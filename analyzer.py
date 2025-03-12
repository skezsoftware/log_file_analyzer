import re
from collections import Counter

def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return len(lines)

def count_keyword_occurrences(file_path, keyword):
    with open(file_path, 'r') as file:
        content = file.read()
    return content.lower().count(keyword.lower())

def most_common_words(file_path, num_words=10):
    with open(file_path, 'r') as file:
        content = file.read()
    words = re.findall(r'\b\w+\b', content.lower())
    counter = Counter(words)
    return counter.most_common(num_words)

def main():
    file_path = input('Enter the path to the log file: ').strip()