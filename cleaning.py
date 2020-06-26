import nltk
import string
f = open('C:\\Users\\User\\Desktop\\corpus\\text.txt', 'r', encoding='utf8')
d = open('C:\\Users\\User\\Desktop\\corpus\\test.txt', 'w', encoding='utf8')
f = f.read()

def clean(text):
    text = text.replace('--', ' ')
    tokens = text.split()
    table = str.maketrans('', '', string.punctuation)
    tokens = [w.translate(table) for w in tokens]
    tokens = [w for w in tokens if w.isalpha()]
    tokens = [w.lower() for w in tokens]
    return tokens

tokens = clean(f)
words = set(tokens)
for i in words:
    x = nltk.FreqDist(tokens)
    d.write('1')
d.close()

