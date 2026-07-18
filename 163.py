# Word frequency calculation
sentence = input("Enter a sentence: ").lower()
words = sentence.split()
word_freq = {}


for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
print("Word Frequencies:")


for word, count in word_freq.items():
    print(f"{word} : {count}")