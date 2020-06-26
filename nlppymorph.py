import nltk
import pymorphy2
b = open('C:\\Users\\User\\Desktop\\corpus\\PoS.txt', 'r', encoding='utf8')
b = b.readlines()
def pos(word):
    morph = pymorphy2.MorphAnalyzer()
    p = morph.parse(word)[0]
    print(p.tag.POS)
for line in b:
    x = nltk.word_tokenize(line)
    
