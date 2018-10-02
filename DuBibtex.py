# DuBibtex
# This script merges duplicated bibtex items from a list of .bib files, capitalize the titles,
# and more importantly, resolve missing DOIs, years.
# This script assumes the first line of each bibtex item contains its bib iD.
# This is typically true if the bibtex item is from Google Scholar or DBLP.
# Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
# Reference: http://www.bibtex.org/Format/
# Sources of DOI: Google, ACM, IEEE, Springer, Caltech, Wiley
import re, requests, json, configparser

__author__ = "Ruofei Du"


class Paras:
    section = "DuBibtex"
    searchDOI = True
    inputFileList = []
    outputFile = ""
    useOfflineDOI = False
    keepComments = False
    debugBibCrawler = True
    debugStatistics = True
    doiJsonFile = ""
    header = {}


def request_url(url):
    return requests.get(url, headers=Paras.header).text


class Re:
    bib = re.compile('\s*\@(\w+)\{([\w\d\.]+),')
    item = re.compile('\s*(\w+)\s*=\s*[\{"]\s*(.*)\s*[\}"],')
    item2 = re.compile('\s*(\w+)\s*=\s*[\{"]\{\s*(.*)\s*[\}"]\}')
    endl = re.compile('\s*}\s*')
    doiJson = re.compile('doi\.org\\?\/([\w\d\.\\\/]*)', flags=re.MULTILINE)
    doiUrl = re.compile('doi\.org\/([\w\d\.\\\/]*)', flags=re.MULTILINE)
    doiJavascript = re.compile('doi\"\:\"([\w\d\.\\\/]*)\"', flags=re.MULTILINE)
    doiText = re.compile('"DOI":"([\w\.\\\/]*)"', flags=re.MULTILINE)
    doiSpringer = re.compile('chapter\/([\w\.\\\/\_\-]*)', flags=re.MULTILINE)
    doiWiley = re.compile('doi\/abs\/([\w\.\\\/\_\-]*)', flags=re.MULTILINE)
    doiCaltech = re.compile('authors\.library\.caltech\.edu\/(\d+)', flags=re.MULTILINE)
    acm = re.compile('citation\.cfm\?id\=(\d+)', flags=re.MULTILINE)
    ieee = re.compile('ieee\.org\/document\/(\d+)', flags=re.MULTILINE)
    year = re.compile('\w+(\d+)')


class Parser:
    fout = None
    bibDict = {}
    doiDict = {}
    duplicated = False
    numMissing, numDuplicated, numFixed = 0, 0, 0
    # current bibitem and bib ID
    cur, bib = None, ''

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        Paras.header['User-Agent'] = config.get(Paras.section, "header").strip()
        Paras.searchDOI = config.getboolean(Paras.section, "searchDOI")
        Paras.useOfflineDOI = config.getboolean(Paras.section, "useOfflineDOI")
        Paras.keepComments = config.getboolean(Paras.section, "keepComments")
        Paras.debugBibCrawler = config.getboolean(Paras.section, "debugBibCrawler")
        Paras.debugStatistics = config.getboolean(Paras.section, "debugStatistics")
        Paras.inputFileList = config.get(Paras.section, "inputFileList").strip().split(",")
        Paras.doiJsonFile = config.get(Paras.section, "doiJsonFile").strip()
        Paras.outputFile = config.get(Paras.section, "outputFile").strip()

        self.fout = open(Paras.outputFile, 'w')
        with open(Paras.doiJsonFile) as f:
            self.doiDict = json.load(f)

    def clear(self):
        self.duplicated = False
        self.bib, self.title = '', ''

    def write_current_item(self):
        self.fout.write('@%s{%s,\n' % (self.cur['type'], self.bib))

        if 'year' not in self.cur:
            m = Re.year.search(self.bib)
            if m and m.groups():
                self.cur['year'] = m.groups()[0]

        if self.bib in self.doiDict:
            if Paras.debugBibCrawler:
                print('Missing DOI, get from local dict.')
            if Paras.debugStatistics:
                self.numMissing += 1
                self.numFixed += 1
            self.cur['doi'] = self.doiDict[self.bib]

        if Paras.searchDOI and 'doi' not in self.cur and self.cur['type'].lower() not in ['misc', 'book']:
            # search for DOI
            if Paras.debugBibCrawler:
                print('Missing DOI, search "%s"...' % self.cur['title'])
            d = google_lookup(self.cur['title'])
            if d:
                self.cur['doi'] = d
            else:
                d = crossref_lookup(self.cur['title'])
                if d:
                    self.cur['doi'] = d
            self.numMissing += 1
            if d:
                self.numFixed += 1

        if 'doi' in self.cur:
            self.cur['doi'] = fix_underscore(self.cur['doi'])
            self.doiDict[self.bib] = self.cur['doi']

        del self.cur['type']
        n = len(self.cur.keys())
        for i, key in enumerate(self.cur.keys()):
            if key in ['booktitle', 'journal', 'title']:
                self.cur[key] = capitalize(self.cur[key])
                # print(cur[key])

            if key in ['title']:
                self.fout.write('  %s={{%s}}' % (key, self.cur[key]))
            else:
                self.fout.write('  %s={%s}' % (key, self.cur[key]))

            if i != n - 1:
                self.fout.write(',')
            self.fout.write('\n')
        self.fout.write('}\n\n')

    def add_new_bib(self, bib_id, bib_type):
        self.bib = bib_id
        if self.bib in self.bibDict:
            self.duplicated = True
            return
        self.bibDict[self.bib] = {}
        self.cur = self.bibDict[self.bib]
        self.cur['type'] = bib_type

    def parse_line(self, line):
        # match EOF
        if Re.endl.match(line):
            if not self.duplicated:
                self.write_current_item()
            self.clear()
            return

        # match duplicates
        if self.duplicated:
            if Paras.debugStatistics:
                print("* duplicated %s" % self.bib)
                self.numDuplicated += 1
            return

        # match new bib item
        m = Re.bib.match(line)
        if m and len(m.groups()) > 0:
            self.add_new_bib(m.groups()[1], m.groups()[0])

        # output comments
        if not self.bib:
            if Paras.keepComments:
                self.fout.write(line)
            return

        # for each bibtex, first match {{}} or {""}, then match {} or ""
        m = Re.item2.match(line)
        if not m:
            m = Re.item.match(line)
        if m and len(m.groups()) > 0:
            self.cur[m.groups()[0]] = m.groups()[1]

    def print_statistics(self):
        print("%d missing doi, %d fixed, %d duplicated" % (self.numMissing, self.numFixed, self.numDuplicated))

    def shut_down(self):
        self.fout.close()
        with open(Paras.doiJsonFile, 'w') as outfile:
            json.dump(self.doiDict, outfile)
            print("Known DOI saved to JSON.")
        self.print_statistics()


def crossref_lookup(_title):
    content = request_url('https://api.crossref.org/works?rows=5&query.title=%s' % _title)
    m = Re.doiJson.search(content)
    if m and len(m.groups()) > 0:
        res = m.groups()[0]
        res = res.replace('\\', '')
        if Paras.debugBibCrawler:
            print("DOI from CrossRef Lookup:", res)
        return res
    return None


def google_lookup(s):
    content = request_url('https://www.google.com/search?q=%s' % s)

    m = Re.doiSpringer.search(content)
    if m and len(m.groups()) > 0:
        res = m.groups()[0].replace('\\', '')
        print("DOI from Google and Springer: %s\n" % res)
        return res

    m = Re.doiWiley.search(content)
    if m and len(m.groups()) > 0:
        res = m.groups()[0].replace('\\', '')
        print("DOI from Google and Wiley: %s\n" % res)
        return res

    m = Re.doiUrl.search(content, re.M)
    if m and len(m.groups()) > 0:
        res = m.groups()[0]
        if Paras.debugBibCrawler:
            print("DOI from Google and DOI.org: %s\n" % res)
        return res

    m = Re.acm.search(content)
    if m and len(m.groups()) > 0:
        content = request_url('https://dl.acm.org/citation.cfm?id=%s' % m.groups()[0])
        m = Re.doiUrl.search(content, re.M)

        if m and len(m.groups()) > 0:
            res = m.groups()[0]
            res = res.replace('\\', '')
            if Paras.debugBibCrawler:
                print("DOI from Google and ACM: %s\n" % res)
            return res

    m = Re.ieee.search(content)
    if m and len(m.groups()) > 0:
        content = request_url('https://ieeexplore.ieee.org/document/%s/' % m.groups()[0])
        m = Re.doiJavascript.search(content, re.M)
        if m and len(m.groups()) > 0:
            res = m.groups()[0].replace('\\', '')
            print("DOI from Google and IEEE: %s\n" % res)
            return res

    m = Re.doiCaltech.search(content)
    if m and len(m.groups()) > 0:
        content = request_url('https://authors.library.caltech.edu/%s/' % m.groups()[0])
        m = Re.doiUrl.search(content, re.M)
        if m and len(m.groups()) > 0:
            res = m.groups()[0]
            res = res.replace('\\', '')
            print("DOI from Google and Caltech: %s\n" % res)
            return res
    return None


def fix_underscore(s):
    return re.sub('[^\_]\_', '\\\_', s)


def capitalize(s, spliter=' '):
    lower_cases = {'a', 'an', 'the', 'to', 'on', 'in', 'of', 'at', 'by', 'for', 'or', 'and', 'vs.'}

    # reverse IEEE conferences
    if s.rfind(',') > 0 and s[-3:].lower() == ' on':
        p = s.rfind(',')
        s = s[p + 2:] + s[:p]

    words = s.split(spliter)
    capitalized_words = []
    for i, word in enumerate(words):
        if len(word) == 0:
            continue
        if 0 < i < len(words) - 1 and word.lower() in lower_cases:
            capitalized_words.append(word.lower())
        else:
            capitalized_words.append(word[0].upper() + word[1:])
    s = spliter.join(capitalized_words)

    return s if spliter == '-' else capitalize(s, '-')


if __name__ == "__main__":
    p = Parser()

    for filename in Paras.inputFileList:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                p.parse_line(line)

    p.shut_down()
