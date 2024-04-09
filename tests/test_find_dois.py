import unittest
import tempfile
import os

import bibtexparser

from DuBibtex import Parser



class TestFindDOIs(unittest.TestCase):

  
  def test_iccv_doi(self):
    filename = "tests/inputs/signet.bib"
    correct_doi = "10.1109/ICCV48922.2021.01396"

    self.assertTrue(os.path.isfile(filename))
    library = bibtexparser.parse_file(filename)

    with tempfile.NamedTemporaryFile() as fp:
        p = Parser(output_file=fp.name)
        for entry in library.entries:
          p.copy_from_parsed_entry(entry)
          p.write_current_item()
        p.shut_down()

        # Check the doi
        generated_library = bibtexparser.parse_file(fp.name)
        self.assertEqual(len(generated_library.entries), len(library.entries), "Number of entries should be the same")
        for entry in generated_library.entries:
          self.assertTrue("doi" in entry)
          self.assertEqual(entry.fields_dict["doi"].value, correct_doi)