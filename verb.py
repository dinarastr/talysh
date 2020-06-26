import nltk
import pymorphy2
a = open('C:\\Users\\User\\Desktop\\corpus\\test.txt', 'r', encoding='utf8')
b = open('C:\\Users\\User\\Desktop\\corpus\\test1.txt', 'w', encoding='utf8')
a = a.readlines()
def pos(word):
    morph = pymorphy2.MorphAnalyzer()
    p = morph.parse(word)[0]
    return p.tag.POS

for line in a:
    x = nltk.word_tokenize(line)
    b.write(pos(x[2

























                  ])+'\n')
b.close()
                
        
