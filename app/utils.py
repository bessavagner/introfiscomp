import re
import unicodedata

def extract_title_from_templates(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.search(r'{% block title %}(.*?)\{% endblock %}', content, re.DOTALL)
        if match:
            return match.group(1).strip()
        else:
            return None


def normalize_string(input_string):
    # Remove accents
    normalized_string = unicodedata.normalize('NFKD', input_string).encode('ASCII', 'ignore').decode('utf-8')
    # Remove special characters
    normalized_string = re.sub(r'[^\w\s-]', '', normalized_string)
    # Convert to lowercase
    normalized_string = normalized_string.lower()
    # Replace spaces with dashes
    normalized_string = re.sub(r'\s+', '-', normalized_string)
    return normalized_string
