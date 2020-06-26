import nltk
f = open('C:\\Users\\User\\Desktop\\corpus\\wordlist.txt', 'r', encoding='utf8')
g = open('C:\\Users\\User\\Desktop\\corpus\\unparsed.txt', 'r', encoding='utf8')
d = open('C:\\Users\\User\\Desktop\\corpus\\parsed.txt', 'w', encoding='utf8')
f = f.readlines()
g = g.read()
g = nltk.word_tokenize(g)
for line in f:
    x = nltk.word_tokenize(line)
    if x[0] not in g:
        d.write(line)
d.close()
