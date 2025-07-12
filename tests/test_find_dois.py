import io
import os
import tempfile

import bibtexparser
import pytest

# Import the main class from your refactored script
from DuBibtex import BibTexManager, _AUTO_COMMENT_CREDIT


def run_doi_check(bibtex_content: str, expected_doi: str):
  """
    A helper function to run the BibTexManager on a string of BibTeX content.

    It processes the content, writes to a temporary file, then reads it back
    to verify that the DOI was correctly found or omitted.

    Args:
        bibtex_content: A string containing one or more BibTeX entries.
        expected_doi: The DOI string that is expected to be in the output.
                      If an empty string, asserts that no DOI was added.
    """
  # Use io.StringIO to treat the string content as a file
  bibtex_file = io.StringIO(bibtex_content)
  library = bibtexparser.load(bibtex_file)

  # Use a temporary file for the output
  with tempfile.NamedTemporaryFile(mode="w+", delete=False) as fp:
    output_filename = fp.name
    manager = BibTexManager(output_file=output_filename, use_offline_doi=False)

    for entry in library.entries:
      # The new, correct method to process an entry
      manager.process_entry(entry)
    manager.shutdown()

  # Read the generated output file and check the DOI
  with open(output_filename, 'r', encoding='utf-8') as f:
    # Skip the auto-generated header comment for parsing
    content = f.read()
    content_without_header = content.replace(_AUTO_COMMENT_CREDIT, "").replace(
        '% https://github.com/ruofeidu/DuBibtex\n', '').strip()
    generated_library = bibtexparser.loads(content_without_header)

  # Clean up the temporary file
  os.remove(output_filename)

  assert len(generated_library.entries) == len(
      library.entries), "Number of entries should be the same"

  # Check each entry for the correct DOI
  for entry in generated_library.entries:
    if expected_doi:
      assert 'doi' in entry, f"DOI field is missing in entry {entry.get('ID')}"
      assert entry['doi'] == expected_doi
    else:
      assert 'doi' not in entry, f"DOI field should not be present in entry {entry.get('ID')}"


# --- Test Cases ---


@pytest.mark.parametrize("bibtex_content, expected_doi", [
    ("""@inproceedings{SIGNET,
        title={{SIGNET: A Simple but Effective Network for Monocular 3D-2D Joint Detection}},
        author={Van, Ngo},
        booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
        year={2021}
    }""", "10.1109/ICCV48922.2021.01396"),
    ("""@inproceedings{qdiffusion,
        title={{Q-Diffusion: Quantizing Diffusion Models}},
        author={Li, Xiuyu},
        booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
        year={2023}
    }""", "10.1109/ICCV51070.2023.01608"),
    ("""@article{holocamera,
        title={{HoloCamera: A Head-Mounted Camera for Egocentric-View 6DoF Video}},
        author={Zeng, Ziyang},
        journal={IEEE Transactions on Visualization and Computer Graphics},
        year={2024}
    }""", "10.1109/TVCG.2024.3372123"),
])
def test_ieee_doi_lookup(bibtex_content, expected_doi):
  """Tests DOI lookup for various IEEE publications (ICCV, TVCG)."""
  run_doi_check(bibtex_content, expected_doi)


@pytest.mark.parametrize("bibtex_content, expected_doi",
                         [("""@inproceedings{nerf,
        title={{NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis}},
        author={Mildenhall, Ben},
        booktitle={European conference on computer vision},
        year={2020}
    }""", "10.1007/978-3-030-58452-8_24")])
def test_crossref_doi_lookup(bibtex_content, expected_doi):
  """Tests DOI lookup using CrossRef for a Springer (ECCV) publication."""
  run_doi_check(bibtex_content, expected_doi)


@pytest.mark.parametrize("bibtex_content, expected_doi",
                         [("""@inproceedings{attention,
      title={{Attention Is All You Need}},
      author={Vaswani, Ashish},
      booktitle={Advances in Neural Information Processing Systems},
      year={2017}
    }""", "10.48550/arXiv.1706.03762")])
def test_arxiv_doi_lookup(bibtex_content, expected_doi):
  """Tests lookup for an arXiv paper, which should generate an arXiv-formatted DOI."""
  run_doi_check(bibtex_content, expected_doi)


@pytest.mark.parametrize(
    "bibtex_content, expected_doi",
    [("""@inproceedings{dragan,
        title={{An Information-Theoretic Approach to Imitation Learning}},
        author={Duan, Yan},
        booktitle={Proceedings of the 36th International Conference on Machine Learning},
        year={2019}
    }""", "")  # This specific ICML paper may not have a DOI assigned.
    ])
def test_no_doi_found(bibtex_content, expected_doi):
  """Tests cases where publications (e.g., from ICML/NeurIPS) might not have a DOI."""
  run_doi_check(bibtex_content, expected_doi)
