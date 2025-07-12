import os
import json
import markdown

FOLDER_NAME = 'sigchi2'


def convert_markdown_to_html(file_path):
  # Read the Markdown file
  with open(file_path, 'r', encoding='utf-8') as file:
    markdown_text = file.read()

  # Convert Markdown to HTML
  html_content = markdown.markdown(markdown_text)

  # Write the HTML content to a new file
  output_file_path = file_path.replace('.md', '.html')
  with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

  print(f"Converted {file_path} to {output_file_path}")


def parse(filename_raw, data, indent=0, program='chi', year='2025'):
  filename = FOLDER_NAME + '/' + filename_raw[:-4] + 'md'

  # with open(filename + 'session.md', 'w', encoding='utf-8') as ff:
  with open(filename, 'w', encoding='utf-8') as f:
    # Iterate over sessions and extract paper titles, session names, and author names
    for session in data['sessions']:
      session_name = session['name']
      if not (session['typeId'] == 13945):  # CHI 2025
        # if not (session['typeId'] == 13748): # UIST 2024
        continue  # Checks if it's a paper session.
      f.write(f"\n## {session_name}\n")
      # ff.write(f"\n## {session_name}\n")
      for content_id in session['contentIds']:
        content = next((c for c in data['contents'] if c['id'] == content_id),
                       None)
        # if content and content['typeId'] in [
        #     13269, 13341
        # ]:  # Check if the content is a paper or journal in CHI

        if content and content['typeId'] in [
            13945
        ]:  # Check if the content is a paper in UIST

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
          id = content['id']
          link = f'https://programs.sigchi.org/{program}/{year}/program/content/{id}'

          f.write(f"### {paper_title}\n")
          if 'award' in content and content['award']:
            f.write(content['award'] + "\n\n")
          f.write(f"Authors: {', '.join(authors)}\n\n")
          f.write(f"[Link]({link})\n\n")
          KEYWORDS = [
              'Reality', 'XR', 'Virtual', 'LLM', 'AI', 'Large', 'Immersive',
              'Communication', 'Gaze', 'Dynamic', 'Perception', 'realities'
          ]
          # if any(keyword in session_name for keyword in KEYWORDS):
          f.write(f"Abstract: {abstract}\n\n")
          f.write('\n\n')

  convert_markdown_to_html(filename)


def read_and_process_json_files(directory_path):
  # Loop through all files in the specified directory
  for filename in os.listdir(directory_path):
    # Check if the file is a JSON file and contains 'CHI_2024' in the filename
    if filename.endswith(".json"):
      filename_raw = filename
      file_path = os.path.join(directory_path, filename)
      # Open and read the JSON file with UTF-8 encoding
      with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Pass the data to the parse function
        parse(filename_raw, data)


# Get the current working directory
current_directory = os.getcwd()
# Specify the directory containing JSON files
directory_path = os.path.join(current_directory, FOLDER_NAME)
read_and_process_json_files(directory_path)
