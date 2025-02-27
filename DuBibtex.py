""" DuBibtex merges duplicated bibtex items and resolve missing DOIs, years, wrong titles, etc.

This script assumes the first line of each bibtex item contains its bib iD.
This is typically true if the bibtex item is from Google Scholar or DBLP.

Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
Reference: http://www.bibtex.org/Format/
Sources of DOI: Google, ACM, IEEE, Springer, Caltech, Wiley
"""
import re
import requests
import json
import configparser

import bibtexparser


class Paras:
  section = "DuBibtex"
  searchDOI = True
  inputFileList = []
  outputFile = ""
  useOfflineDOI = False
  printSelfInfo = True
  keepComments = False
  debugBibCrawler = True
  debugStatistics = True
  defaultAddress = True
  defaultPublisher = True
  doiJsonFile = ""
  minYear = 1946
  timeOut = 3
  header = {}
  DOI2URL = False
  removeUrl = False
  # If optimizeBibId is True, orename Bib Id into LastName2000FirstTitleWord
  optimizeBibId = False
  fieldRemovalList = []
  autoCommentCredit = '% Automatically generated by DuBibTeX.\n'
  autoCommentUrl = '% https://github.com/ruofeidu/DuBibtex\n'


def request_url(url):
  return requests.get(url, headers=Paras.header).text


class Re:
  bib = re.compile(r'\s*\@(\w+)\s*\{\s*([^\{\,\}]+),')
  item = re.compile(r'\s*(\w+)\s*=\s*[\{"]\s*(.*)\s*[\}"]')
  item2 = re.compile(r'\s*(\w+)\s*=\s*[\{"]\{\s*(.*)\s*[\}"]\}')
  endl = re.compile(r'\s*}\s*')
  abbr = re.compile(r'@string', flags=re.IGNORECASE)
  doiJson = re.compile(r'doi\.org\\?\/([\w\d\.\-\\\/]+)', flags=re.MULTILINE)
  doiUrl = re.compile(r'rdoi\.org\/([\w\d\.\-\\\/]+)', flags=re.MULTILINE)
  doiAcmUrl = re.compile(
      r'https:\/\/dl\.acm\.org\/doi\/(?:\w+\/)?([\w\d\.\-\\\/]+)',
      flags=re.MULTILINE)
  doiJavascript = re.compile(r'doi\"\:\"([\w\d\.\-\\\/]+)\"',
                             flags=re.MULTILINE)
  doiText = re.compile(r'"DOI":"([\w\.\\\/]*)"', flags=re.MULTILINE)
  doiSpringer = re.compile(r'chapter\/([\w\.\\\/\_\-]+)', flags=re.MULTILINE)
  doiWiley = re.compile(r'doi\/abs\/([\w\.\\\/\_\-]+)', flags=re.MULTILINE)
  doiCaltech = re.compile(r'authors\.library\.caltech\.edu\/(\d+)',
                          flags=re.MULTILINE)
  doiPubmed = re.compile(r'nlm\.nih\.gov\/pubmed\/(\d+)', flags=re.MULTILINE)
  urlArxiv = re.compile(r'arxiv\.org\/pdf\/([\d\.]+)', flags=re.MULTILINE)
  acm = re.compile(r'citation\.cfm\?id\=([\d\.]+)', flags=re.MULTILINE)
  acmBib = re.compile(r'<PRE id="[\d\.]+">(.+)<\/pre>',
                      flags=re.MULTILINE | re.IGNORECASE | re.S)
  ieee = re.compile(r'ieee\.org(?:\/abstract)?\/document\/(\d+)',
                    flags=re.MULTILINE)
  neurips = re.compile(r'proceedings.neurips.cc', flags=re.MULTILINE)
  year = re.compile(r'\w+(\d+)')


class Parser:
  fout = None
  bibDict = {}
  doiDict = {}
  duplicated = False
  # abbreviation: @String(PAMI = {IEEE Trans. Pattern Anal. Mach. Intell.})
  abbreviations = ''
  numMissing, numDuplicated, numFixed = 0, 0, 0
  # current bibitem and bib ID
  cur, bib = None, ''

  def __init__(self, output_file=None, use_offline_doi=None):
    config = configparser.ConfigParser()
    config.read("config.ini")
    Paras.header['User-Agent'] = config.get(Paras.section, "header").strip()
    Paras.searchDOI = config.getboolean(Paras.section, "searchDOI")
    Paras.useOfflineDOI = use_offline_doi if use_offline_doi is not None else config.getboolean(
        Paras.section, "useOfflineDOI")
    Paras.printSelfInfo = config.getboolean(Paras.section, "printSelfInfo")
    Paras.keepComments = config.getboolean(Paras.section, "keepComments")
    Paras.debugBibCrawler = config.getboolean(Paras.section, "debugBibCrawler")
    Paras.debugStatistics = config.getboolean(Paras.section, "debugStatistics")
    Paras.optimizeBibId = config.getboolean(Paras.section, "optimizeBibId")
    Paras.inputFileList = config.get(Paras.section,
                                     "inputFileList").strip().split(",")
    Paras.doiJsonFile = config.get(Paras.section, "doiJsonFile").strip()
    Paras.outputFile = output_file if output_file else config.get(
        Paras.section, "outputFile").strip()
    Paras.fieldRemovalList = config.get(Paras.section,
                                        "fieldRemovalList").strip().split(",")
    Paras.minYear = config.getint(Paras.section, "minYear")
    Paras.timeOut = config.getint(Paras.section, "timeOut")
    Paras.DOI2URL = config.getboolean(Paras.section, "DOI2URL")
    Paras.defaultAddress = config.getboolean(Paras.section, "defaultAddress")

    self.fout = open(Paras.outputFile, 'w', encoding='utf8')
    if Paras.printSelfInfo:
      self.fout.write('%s%s' % (Paras.autoCommentCredit, Paras.autoCommentUrl))
    if Paras.useOfflineDOI:
      with open(Paras.doiJsonFile, encoding='utf8') as f:
        self.doiDict = json.load(f)

  def clear(self):
    self.duplicated = False
    self.bib = ''

  def debug_bib(self, s):
    if not Paras.debugBibCrawler:
      return
    print(s)

  def fix_doi(self, _doi):
    if Paras.debugStatistics:
      self.numMissing += 1
      self.numFixed += 1
    if len(_doi) > 4 and (_doi[:3] == 'pdf' or _doi[:3] == 'abs'):
      _doi = _doi[4:]
    self.cur['doi'] = _doi
    if Paras.DOI2URL:
      self.cur['url'] = 'http://doi.org/%s' % _doi

  def write_current_item(self):
    # print(self.cur)
    self.debug_bib(self.cur['title'])

    # Ensures there is year field.
    if 'year' not in self.cur or len(self.cur['year']) < 4:
      m = Re.year.search(self.bib)
      if m and m.groups():
        self.cur['year'] = m.groups()[0]
      else:
        print('warning of empty year: ', self.cur['title'])
        self.cur['year'] = 2022

    # Optimizes self.bib id.
    if Paras.optimizeBibId and 'author' in self.cur and 'title' in self.cur and 'year' in self.cur:
      self.bib = self.cur['author'].split(
          ',', 1)[0] + self.cur['year'] + self.cur['title'].split(
              ' ', 1)[0].capitalize()

    if not 'author' in self.cur:
      print('Error: No author for ' + self.bib)

    if not 'title' in self.cur:
      print('Error: No title for ' + self.bib)

    if not 'year' in self.cur:
      print('Error: No year for ' + self.bib)

    self.fout.write('@%s{%s,\n' % (self.cur['type'].lower(), self.bib))

    if Paras.defaultAddress and 'address' not in self.cur:
      self.cur['address'] = 'New York, NY, USA'

    if self.cur['type'] == 'article' and 'address' in self.cur:
      del self.cur['address']

    if Paras.defaultPublisher and 'publisher' not in self.cur:
      if 'organization' in self.cur:
        self.cur['publisher'] = self.cur['organization']
      elif 'journal' in self.cur and self.cur['journal'][:5] == 'arXiv':
        self.cur['publisher'] = 'arXiv'
      else:
        self.debug_bib('PUB\t' + self.cur['title'])
        # self.cur['publisher'] = 'ACM'

    if self.bib in self.doiDict and ('doi' not in self.cur or
                                     not self.cur['doi']):
      self.debug_bib('Missing DOI, but obtained from the local dict JSON.')
      self.fix_doi(self.doiDict[self.bib])

    # Removes invalid DOI field.
    if 'doi' in self.cur and '/' not in self.cur['doi']:
      del self.cur['doi']
    # if self.cur['type'].lower() in ['misc', 'book'] and 'doi' in self.cur:
    #   del self.cur['doi']

    # Searches DOI field if the field was missing.
    if Paras.searchDOI and int(self.cur['year']) > Paras.minYear and 'doi' not in self.cur \
            and self.cur['type'].lower() not in ['misc', 'book', 'techreport'] and 'nodoi' not in self.cur:
      # Searches for DOI.
      self.debug_bib('Missing DOI, search "%s"...' % self.cur['title'])

      title_without_brackets = re.sub(r'\{|\}', '', self.cur['title'])
      if ('journal' in self.cur and
          any([x in self.cur['journal'].lower() for x in ["ieee"]]) or
          'booktitle' in self.cur and
          any([x in self.cur['booktitle'].lower() for x in ["ieee", "iccv"]])):
        d = ieee_xplore_lookup(title_without_brackets, self)
        if d:
          self.fix_doi(d)
        else:
          self.numMissing += 1
      elif 'journal' in self.cur and self.cur['journal'][:5].lower() == 'arxiv':
        content = request_url('https://www.google.com/search?q=%s' %
                              title_without_brackets)
        m = Re.urlArxiv.search(content)
        if m and len(m.groups()) > 0:
          self.cur['url'] = "https://arxiv.org/pdf/%s" % m.groups()[0]
          self.debug_bib('Missing DOI, search "%s"...' % title_without_brackets)
      else:
        d = google_lookup(title_without_brackets, self)
        if not d:
          d = crossref_lookup(title_without_brackets)
        if d:
          self.fix_doi(d)
        else:
          self.numMissing += 1

    # Fixes underscore and stores it in the hash table.
    if 'doi' in self.cur:
      self.cur['doi'] = fix_underscore(self.cur['doi'])
      self.cur['doi'] = fix_abs_pdf(self.cur['doi'])
      self.doiDict[self.bib] = self.cur['doi']

    del self.cur['type']
    if Paras.removeUrl and 'url' in self.cur:
      del self.cur['url']

    n = len(self.cur.keys())
    for i, key in enumerate(self.cur.keys()):
      if key in Paras.fieldRemovalList:
        continue
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
    if self.bib.lower() in self.bibDict:
      self.duplicated = True
      return
    self.bibDict[self.bib.lower()] = {}
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

    if Re.abbr.match(line):
      # abbreciation
      self.fout.write(line)
      return

    # Matches duplicates.
    if self.duplicated:
      if Paras.debugStatistics:
        print("* duplicated %s" % self.bib)
        self.numDuplicated += 1
      return

    # Matches new bib item with type and bib id.
    m = Re.bib.match(line)
    if m and len(m.groups()) > 0:
      self.add_new_bib(m.groups()[1], m.groups()[0])

    # Outputs comments when required.
    if not self.bib:
      if Paras.keepComments and line != Paras.autoCommentCredit and line != Paras.autoCommentUrl and len(
          line) > 2:
        self.fout.write(line)
      return

    # For each bibtex, first matches {{}} or {""}, then matches {} or "".
    m = Re.item2.match(line)
    if not m:
      m = Re.item.match(line)
    if m and len(m.groups()) > 0:
      self.cur[m.groups()[0].lower()] = m.groups()[1]

  def copy_from_parsed_entry(self, entry):
    self.add_new_bib(entry.key, entry.entry_type)
    for field in entry.fields:
      self.cur[field.key] = field.value

  def print_statistics(self):
    print("%d missing doi, %d fixed, %d duplicated" %
          (self.numMissing, self.numFixed, self.numDuplicated))

  def shut_down(self):
    self.fout.close()
    if Paras.useOfflineDOI:
      with open(Paras.doiJsonFile, 'w', encoding='utf8') as outfile:
        json.dump(self.doiDict, outfile)
        print("DuBibTeX has saved known DOI to %s." % Paras.doiJsonFile)
    self.print_statistics()


def crossref_lookup(_title):
  content = request_url('https://api.crossref.org/works?rows=5&query.title=%s' %
                        _title)
  m = Re.doiJson.search(content)
  if m and len(m.groups()) > 0:
    res = m.groups()[0]
    res = res.replace('\\', '')
    if 'policy' not in res:
      if Paras.debugBibCrawler:
        print("DOI from CrossRef Lookup: %s\n" % res)
      return res
  return None


def levenshtein(s1, s2):
  s1 = s1.lower()
  s2 = s2.lower()
  if len(s1) < len(s2):
    return levenshtein(s2, s1)

  if len(s2) == 0:
    return len(s1)

  previous_row = range(len(s2) + 1)
  for i, c1 in enumerate(s1):
    current_row = [i + 1]
    for j, c2 in enumerate(s2):
      insertions = previous_row[j + 1] + 1
      deletions = current_row[j] + 1
      substitutions = previous_row[j] + (c1 != c2)
      current_row.append(min(insertions, deletions, substitutions))
    previous_row = current_row

  return previous_row[-1]


def ieee_xplore_lookup(s, parser):
  # Search IEEE Xplore
  xplore_search_url = 'https://ieeexplore.ieee.org/rest/search'
  payload = {
      "newsearch": "true",
      "queryText": s,
      "highlight": "true",
      "returnFacets": ["ALL"],
      "returnType": "SEARCH",
      "matchPubs": "true"
  }
  response = requests.post(
      xplore_search_url,
      json=payload,
      headers={
          "User-Agent":
              Paras.header["User-Agent"],
          "Origin":
              "https://ieeexplore.ieee.org",
          "Referer":
              "https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText="
      })
  try:
    result = response.json()
    if result["records"]:
      return result["records"][0]["doi"]
  except Exception as e:
    pass
  return None


def google_lookup_ieee_only(s, parser):
  # Search Google with IEEE keyword
  html = request_url('https://www.google.com/search?q=ieee+%s' % s)
  m = Re.ieee.search(html)
  if m and len(m.groups()) > 0:
    html_ieee = request_url('https://ieeexplore.ieee.org/document/%s' %
                            m.groups()[0])
    m = Re.doiJavascript.search(html_ieee, re.M)
    if m and len(m.groups()) > 0:
      res = m.groups()[0].replace('\\', '')
      print("DOI from Google and IEEE: %s\n" % res)
      return res
  return None


def google_lookup(s, parser):
  html = request_url('https://www.google.com/search?q=%s' % s)
  with open('debug.txt', 'w', encoding='utf8') as f:
    f.write(html)

  url_regexes = [
      'doiAcmUrl', 'acm', 'doiSpringer', 'doiWiley', 'doiUrl', 'ieee',
      'doiCaltech', 'doiPubmed', 'neurips'
  ]

  found_urls = []
  for url_regex in url_regexes:
    m = getattr(Re, url_regex).search(html)
    if m:
      print("Found URL: %s" % url_regex)
      found_urls.append((url_regex, m, m.start()))
  # Sort by start position
  found_urls.sort(key=lambda x: x[2])

  for url_regex, m, _ in found_urls:

    if url_regex == 'neurips':
      # NeurIPS does not have a DOI.
      return None

    if url_regex == 'doiAcmUrl' and m and len(m.groups()) > 0:
      res = m.groups()[0].replace('\\', '')
      print("DOI from Google and ACM DOI: %s\n" % res)
      if res.startswith('10.5555'):
        # ACM DOI is not valid. 5555 is a test DOI.
        return None
      return res

    if url_regex == 'acm' and m and len(m.groups()) > 0:
      # print(m.groups()[0])
      content_acm = request_url('https://dl.acm.org/citation.cfm?id=%s' %
                                m.groups()[0])
      m = Re.doiUrl.search(content_acm, re.M)
      if m and len(m.groups()) > 0:
        print(m.groups()[0])
        res = m.groups()[0]
        if Paras.debugBibCrawler:
          print("DOI from Google and ACM CFM: %s\n" % res)
        return res
      # content_acm = request_url(
      #     'https://dl.acm.org/exportformats.cfm?id=%s&expformat=bibtex' %
      #     m.groups()[0])
      # m = Re.acmBib.search(content_acm, re.M)
      # # TODO: month
      # if m and len(m.groups()) > 0:
      #   acm_lines = m.groups()[0].splitlines()
      #   res = ''
      #   for l in acm_lines:
      #     if len(l) < 3 or l[0] == '@' or l[0] == '}':
      #       continue
      #     mm = Re.item.search(l)
      #     old_cur = parser.cur.copy()
      #     if mm and len(mm.groups()) > 0:
      #       cur_left, cur_right = mm.groups()[0].strip(), mm.groups()[1].strip()
      #       if cur_left == 'doi':
      #         res = cur_right
      #       if cur_left in ['class', 'href', 'doi', 'numpages']:
      #         continue
      #       parser.cur[cur_left] = cur_right

      #   dist = levenshtein(old_cur['title'], parser.cur['title'])
      #   print(dist, old_cur['title'], parser.cur['title'])
      #   if dist > 2:
      #     parser.cur = old_cur
      #     res = ''

      #   if res:
      #     if Paras.debugBibCrawler:
      #       print("DOI from Google and ACM BibTeX: %s\n" % res)
      #     return res

    if url_regex == 'doiSpringer' and m and len(m.groups()) > 0:
      res = m.groups()[0].replace('\\', '')
      print("DOI from Google and Springer: %s\n" % res)
      return res

    if url_regex == 'doiWiley' and m and len(m.groups()) > 0:
      res = m.groups()[0].replace('\\', '')
      print("DOI from Google and Wiley: %s\n" % res)
      return res

    if url_regex == 'doiUrl' and m and len(m.groups()) > 0:
      res = m.groups()[0]
      if Paras.debugBibCrawler:
        print("DOI from Google and DOI.org: %s\n" % res)
      return res

    if url_regex == 'ieee' and m and len(m.groups()) > 0:
      html_ieee = request_url('https://ieeexplore.ieee.org/document/%s' %
                              m.groups()[0])
      m = Re.doiJavascript.search(html_ieee, re.M)
      if m and len(m.groups()) > 0:
        res = m.groups()[0].replace('\\', '')
        print("DOI from Google and IEEE: %s\n" % res)
        return res

    if url_regex == 'doiCaltech' and m and len(m.groups()) > 0:
      html_cal = request_url('https://authors.library.caltech.edu/%s' %
                             m.groups()[0])
      m = Re.doiUrl.search(html_cal, re.M)
      if m and len(m.groups()) > 0:
        res = m.groups()[0]
        res = res.replace('\\', '')
        print("DOI from Google and Caltech: %s\n" % res)
        return res

    if url_regex == 'doiPubmed' and m and len(m.groups()) > 0:
      html_pubmed = request_url('https://www.ncbi.nlm.nih.gov/pubmed/%s' %
                                m.groups()[0])
      m = Re.doiUrl.search(html_pubmed, re.M)
      if m and len(m.groups()) > 0:
        res = m.groups()[0]
        res = res.replace('\\', '')
        print("DOI from Google and PubMed: %s\n" % res)
        return res

  # Nowadays, CVPR papers are hard to fetch DOI without ieee keyword.
  html = request_url('https://www.google.com/search?q=ieee+%s' % s)
  m = Re.ieee.search(html)
  if m and len(m.groups()) > 0:
    html_ieee = request_url('https://ieeexplore.ieee.org/document/%s' %
                            m.groups()[0])
    m = Re.doiJavascript.search(html_ieee, re.M)
    if m and len(m.groups()) > 0:
      res = m.groups()[0].replace('\\', '')
      print("DOI from Google and IEEE (2): %s\n" % res)
      return res

  print("* Nothing was found.\n")
  return None


def fix_underscore(s):
  return re.sub(r'[^\_]\_', r'\\\_', s)


def fix_abs_pdf(s):
  return s


def capitalize(s, spliter=' '):
  SPECIAL_WORDS = [
      'a', 'an', 'the', 'to', 'on', 'in', 'of', 'at', 'by', 'for', 'or', 'and',
      'vs.', 'iOS', '2D', '3D', '4D', '6DoF', 'via'
  ]

  SPECIAL_WORDS_LOWER = list(map(lambda x: x.lower(), SPECIAL_WORDS))
  LOWER_CASES = dict(zip(SPECIAL_WORDS, SPECIAL_WORDS_LOWER))

  s = s.strip(',.- ')
  # Reverses wrong order for IEEE proceedings.
  # if comma is found and last word is 'on'.
  if s.rfind(',') > 0 and s[-3:].lower() == ' on':
    p = s.rfind(',')
    s = s[p + 2:] + s[:p]

  # Split the words and capitalize with filters.
  words = s.split(spliter)
  capitalized_words = []
  start = True
  for word in words:
    if len(word) == 0:
      continue
    if not start and word.lower() in LOWER_CASES:
      capitalized_words.append(LOWER_CASES[word.lower()])
    else:
      capitalized_words.append(word[0].upper() + word[1:])
    start = word[-1] in '.:'

  s = spliter.join(capitalized_words)

  return s if spliter == '-' else capitalize(s, '-')


if __name__ == "__main__":
  p = Parser()

  for filename in Paras.inputFileList:
    library = bibtexparser.parse_file(filename)
    for entry in library.entries:
      p.copy_from_parsed_entry(entry)
      p.write_current_item()

  p.shut_down()
