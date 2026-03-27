import json
import os

import markdown

# Program and year constants.
PROGRAM = 'chi'
YEAR = '2026'

# Session and content type constants for CHI 2026.
SESSION_TYPE_ID = 14694
CONTENT_TYPE_IDS = [14694]

# Folder name for input/output.
FOLDER_NAME = 'sigchi-latest'

# Keywords for abstract filtering (optional).
KEYWORDS = [
    'Reality', 'XR', 'Virtual', 'LLM', 'AI', 'Large', 'Immersive',
    'Communication', 'Gaze', 'Dynamic', 'Perception', 'realities'
]


def convert_markdown_to_html(file_path):
  """Converts a Markdown file to an HTML file."""
  # Reads the Markdown file.
  with open(file_path, 'r', encoding='utf-8') as file:
    markdown_text = file.read()

  # Converts Markdown to HTML.
  html_content = markdown.markdown(markdown_text)

  # Writes the HTML content to a new file.
  output_file_path = file_path.replace('.md', '.html')
  with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

  print(f"Converted {file_path} to {output_file_path}")


def parse(filename_raw, data):
  """Parses the SIGCHI program data and writes to a Markdown file."""
  filename = FOLDER_NAME + '/' + filename_raw[:-4] + 'md'

  with open(filename, 'w', encoding='utf-8') as f:
    # Filters and sorts sessions based on keywords.
    valid_sessions = [
        s for s in data['sessions'] if s.get('typeId') == SESSION_TYPE_ID
    ]

    def get_sort_key(session):
      name = session['name'].lower()
      for i, kw in enumerate(KEYWORDS):
        if kw.lower() in name:
          return (0, i, name)
      return (1, len(KEYWORDS), name)

    valid_sessions.sort(key=get_sort_key)

    # Iterates over sorted sessions and extracts paper titles, names, and authors.
    for session in valid_sessions:
      session_name = session['name']

      f.write(f"\n## {session_name}\n")
      for content_id in session['contentIds']:
        content = next((c for c in data['contents'] if c['id'] == content_id),
                       None)

        if content and content['typeId'] in CONTENT_TYPE_IDS:
          paper_title = content['title']
          authors = []
          for author in content['authors']:
            person = next(
                (p for p in data['people'] if p['id'] == author['personId']),
                None)
            if person:
              author_name = f"{person['firstName']} {person['lastName']}"
              authors.append(author_name)

          abstract = content['abstract']
          content_id_val = content['id']
          link = (f'https://programs.sigchi.org/{PROGRAM}/{YEAR}/'
                  f'program/content/{content_id_val}')

          f.write(f"### {paper_title}\n")
          if 'award' in content and content['award']:
            f.write(content['award'] + "\n\n")
          f.write(f"Authors: {', '.join(authors)}\n\n")
          f.write(f"[Link]({link})\n\n")
          f.write(f"Abstract: {abstract}\n\n")
          f.write('\n\n')

  convert_markdown_to_html(filename)


def read_and_process_json_files(directory_path):
  """Loops through all JSON files in the directory and parses them."""
  # Loops through all files in the specified directory.
  for filename in os.listdir(directory_path):
    # Checks if the file is a JSON file and contains 'CHI_2024' in the filename.
    if filename.endswith(".json"):
      filename_raw = filename
      file_path = os.path.join(directory_path, filename)
      # Opens and reads the JSON file with UTF-8 encoding.
      with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Passes the data to the parse function.
        parse(filename_raw, data)


if __name__ == "__main__":
  # Gets the current working directory.
  current_directory = os.getcwd()
  # Specifies the directory containing JSON files.
  data_directory_path = os.path.join(current_directory, FOLDER_NAME)
  read_and_process_json_files(data_directory_path)

