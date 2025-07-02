from collections import Counter
text = input("Enter a Text: ")
counter = Counter(text)
print("Characters frequencies: ",  dict(counter))