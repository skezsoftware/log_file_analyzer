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

    while True:
        print("\nLog File Analyzer")
        print("1. Count Lines")
        print("2. Count Keyword Occurrences")
        print("3. Most Common Words")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            lines_count = count_lines(file_path)
            print(f"Number of lines: {lines_count}")
        elif choice == '2':
            keyword = input("Enter the keyword to search for: ").strip()
            keyword_count = count_keyword_occurrences(file_path, keyword)
            print(f"Occurences of: '{keyword}': {keyword_count}")
        elif choice == '3':
            num_words = int(input("Enter the number of most common words to display").strip())
            common_words = most_common_words(file_path, num_words)
            print(f"Most common words: {common_words}")
        elif choice == '4':
            print("Exiting the analyer.")
            break
        else:
            print("Invald choice. Please try again.")

if __name__=="__main__":
    main()