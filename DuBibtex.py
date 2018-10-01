# Merge duplicated bibtex, capitalize the titles, and resolve missing DOI
import re, requests

SEARCH_DOI = True
# Reference: http://www.bibtex.org/Format/

re_id = re.compile('\s*\@(\w+)\{([\w\d\.]+),')
re_item = re.compile('\s*(\w+)\s*=\s*[\{"]+([^\}]*)\s*[\}"]+')
re_end = re.compile('\s*}\s*')
re_doi = re.compile('doi\.org\\?\/([\w\d\.\\\/]*)', flags=re.MULTILINE)
re_doi3 = re.compile('doi\.org\/([\w\d\.\\\/]*)', flags=re.MULTILINE)
re_doi2 = re.compile('"DOI":"([\w\.\\\/]*)"', flags=re.MULTILINE)
re_doi_springer = re.compile('chapter\/([\w\.\\\/\_\-]*)', flags=re.MULTILINE)
re_acm = re.compile('citation\.cfm\?id\=(\d+)', flags=re.MULTILINE)

bib_set = {}
bib = ''
duplicated = False
hasDOI = False
doi = ''
title = ''
cur = None
fout = open('output.bib', 'w')
num_missing, num_duplicated, num_fixed = 0, 0, 0
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}


def crossref_lookup(s):
    global header
    url = 'https://api.crossref.org/works?rows=5&query.title=%s' % s
    content = requests.get(url, headers=header).text
    # content = open('example.txt', 'r').readline()
    print(content)
    m = re_doi2.search(content)

    m = re_doi.search(content)
    if m and len(m.groups()) > 0:
        res = m.groups()[0]
        res = res.replace('\\', '')
        print(res)
        return res
    return None


def google_loopup(s):
    url = 'https://www.google.com/search?q=%s' % s
    content = requests.get(url, headers=header).text
    m = re_doi_springer.search(content)

    if m and len(m.groups()) > 0:
        res = m.groups()[0]
        res = res.replace('\\', '')
        print("DOI from Google and Springer: %s\n" % res)
        return res

    m = re_doi3.search(content, re.M)
    if m and len(m.groups()) > 0:
        res = m.groups()[0]
        print("DOI from Google and DOI.org: %s\n" % res)
        return res

    m = re_acm.search(content)
    if m and len(m.groups()) > 0:
        res = m.groups()[0]
        url = 'https://dl.acm.org/citation.cfm?id=%s' % res
        content = requests.get(url, headers=header).text
        # content = ''.join(open('example.txt', 'r').readlines())
        m = re_doi3.search(content, re.M)
        # print("content", content)

        if m and len(m.groups()) > 0:
            res = m.groups()[0]
            res = res.replace('\\', '')
            print("DOI from Google and ACM: %s\n" % res)

        return res
    return None


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


def output(fout, cur, bib):
    global num_missing, num_fixed

    fout.write('@%s{%s,\n' % (cur['type'], bib))
    del cur['type']

    if SEARCH_DOI and doi not in cur:
        # search for DOI
        print('Missing DOI, search "%s"...' % cur['title'])
        d = google_loopup(cur['title'])
        if d:
            cur['doi'] = d
        else:
            d = crossref_lookup(cur['title'])
            if d:
                cur['doi'] = d
        num_missing += 1
        num_fixed += 1
        # if num_fixed > 9:
        #     exit(0)

    n = cur.keys()
    for i, key in enumerate(cur.keys()):
        if key in ['booktitle', 'journal', 'title']:
            cur[key] = capitalize(cur[key])
            # print(cur[key])

        if key == 'title':
            fout.write('  %s={{%s}}' % (key, cur[key]))
        else:
            fout.write('  %s={%s}' % (key, cur[key]))

        if i != n:
            fout.write(',\n')
        else:
            fout.write('\n')
    fout.write('}\n\n')


with open('input.bib', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if re_end.match(line):
            if not duplicated:
                output(fout, cur, bib)

            duplicated = False
            doi, title = '', ''
            continue
        if duplicated:
            print("* duplicated %s" % bib)
            num_duplicated += 1
            continue

        m = re_id.match(line)
        if m and len(m.groups()) > 0:
            bib = m.groups()[1]
            if bib in bib_set:
                duplicated = True
                continue
            bib_set[bib] = {}
            cur = bib_set[bib]
            cur['type'] = m.groups()[0]
            print(bib)

        if not bib:
            fout.write(line)
            continue

        m = re_item.match(line)
        if m and len(m.groups()) > 0:
            cur[m.groups()[0]] = m.groups()[1]

fout.close()

print("%d missing doi, %d fixed, %d duplicated" % (num_missing, num_fixed, num_duplicated))
