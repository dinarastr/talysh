import nltk
g = open('C:\\Users\\User\\Desktop\\corpus\\priorities.txt', 'r', encoding='utf8')
g = g.readlines()
x = []
y = []
for line in g:
    i = nltk.word_tokenize(line)
    x.append(i[0])
    y.append(int(i[1]))
    slovar = dict(zip(x, y))
sort = sorted(slovar.items(), key=lambda i: i[1], reverse=True)
print(sort[:40])
    
         
