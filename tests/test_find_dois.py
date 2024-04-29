import tempfile
import os

import bibtexparser
import pytest

from DuBibtex import Parser


def search_and_check_doi(filename, correct_doi):
  input_file = os.path.join("tests", "inputs", filename)

  assert os.path.isfile(input_file), f"File {input_file} does not exist"
  library = bibtexparser.parse_file(input_file)

  with tempfile.NamedTemporaryFile() as fp:
    p = Parser(output_file=fp.name, use_offline_doi=False)
    for entry in library.entries:
      p.copy_from_parsed_entry(entry)
      p.write_current_item()
    p.shut_down()

    # Check the doi
    generated_library = bibtexparser.parse_file(fp.name)
    assert len(generated_library.entries) == len(
        library.entries), "Number of entries should be the same"
    for entry in generated_library.entries:
      if correct_doi:
        assert "doi" in entry
        assert entry.fields_dict["doi"].value == correct_doi
      else:
        assert "doi" not in entry


@pytest.mark.parametrize("filename,correct_doi", [
    ("signet.bib", "10.1109/ICCV48922.2021.01396"),
    ("qdiffusion.bib", "10.1109/ICCV51070.2023.01608"),
])
def test_iccv_doi(filename, correct_doi):
  search_and_check_doi(filename, correct_doi)


@pytest.mark.parametrize("filename,correct_doi", [
    ("holocamera.bib", "10.1109/TVCG.2024.3372123"),
])
def test_tvcg_doi(filename, correct_doi):
  search_and_check_doi(filename, correct_doi)


@pytest.mark.parametrize("filename", [
    ("ddpm.bib"),
])
def test_neurips_doi(filename):
  # NeurIPS does not have a DOI
  search_and_check_doi(filename, "")


@pytest.mark.parametrize("filename", [
    ("diffusion.bib"),
])
def test_icml_doi(filename):
  # ICML does not have a DOI
  search_and_check_doi(filename, "")
