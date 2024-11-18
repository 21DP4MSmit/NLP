import re

def main():
    raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
    
    # Remove mentions, URLs, and special characters
    cleaned_text = re.sub(r'@\w+|http\S+|[^a-zA-Zā-žĀ-Ž\s]', '', raw_text).lower().strip()
    
    print(cleaned_text)
