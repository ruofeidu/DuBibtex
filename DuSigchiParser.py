import os
import json
import markdown


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


def parse(filename_raw, data, indent=0, program='chi', year='2024'):
  filename = 'sigchi/' + filename_raw[:-4] + 'md'
  with open(filename, 'w', encoding='utf-8') as f:
    # Iterate over sessions and extract paper titles, session names, and author names
    for session in data['sessions']:
      session_name = session['name']
      if not (session['typeId'] == 13269):
        continue  # Checks if it's a paper session.
      f.write(f"\n## {session_name}\n")
      for content_id in session['contentIds']:
        content = next((c for c in data['contents'] if c['id'] == content_id),
                       None)
        if content and content[
            'typeId'] == 13269:  # Check if the content is a paper
          paper_title = content['title']
          authors = [
              f"{person['firstName']} {person['lastName']}"
              for person in data['people']
              if person['id'] in
              [author['personId'] for author in content['authors']]
          ]
          abstract = content['abstract']
          id = content['id']
          link = f'https://programs.sigchi.org/{program}/{year}/program/content/{id}'

          f.write(f"### {paper_title}\n")
          if 'award' in content and content['award']:
            f.write(content['award'] + "\n\n")
          f.write(f"Authors: {', '.join(authors)}\n\n")
          f.write(f"[Link]({link})\n\n")
          f.write(f"Abstract: {abstract}\n\n")
          f.write('\n\n')

  convert_markdown_to_html(filename)


def read_and_process_json_files(directory_path):
  # Loop through all files in the specified directory
  for filename in os.listdir(directory_path):
    # Check if the file is a JSON file and contains 'CHI_2024' in the filename
    if filename.endswith(".json") and "CHI_2024" in filename:
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
directory_path = os.path.join(current_directory, "sigchi/")
read_and_process_json_files(directory_path)
