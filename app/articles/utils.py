import re

def replace_tags(text):

    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!`)(?<!_)`([^`]*?)`(?<!`)', r'<code>\1</code>', text)
    text = re.sub(r'(?<!`)(?<!_)`([^`]*?)`', r'<code>\1</code>', text)

    return text

def naive_senences(text):

    return re.split(r'\.\s|\.\n', text)
