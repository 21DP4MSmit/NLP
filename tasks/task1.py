from collections import Counter
import re

def main():
    text = ("Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. "
            "Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem.")
    
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)
    
    print("Vārdu biežums:", word_counts)
