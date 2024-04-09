import tempfile
import os

import bibtexparser
import pytest

from DuBibtex import Parser


@pytest.mark.parametrize("filename,correct_doi", [
    ("signet.bib", "10.1109/ICCV48922.2021.01396"),
])
def test_iccv_doi(filename, correct_doi):
    input_file = os.path.join("tests", "inputs", filename)

    assert os.path.isfile(input_file), f"File {input_file} does not exist"
    library = bibtexparser.parse_file(input_file)

    with tempfile.NamedTemporaryFile() as fp:
        p = Parser(output_file=fp.name)
        for entry in library.entries:
            p.copy_from_parsed_entry(entry)
            p.write_current_item()
        p.shut_down()

        # Check the doi
        generated_library = bibtexparser.parse_file(fp.name)
        assert len(generated_library.entries) == len(
            library.entries), "Number of entries should be the same"
        for entry in generated_library.entries:
            assert "doi" in entry
            assert entry.fields_dict["doi"].value == correct_doi
