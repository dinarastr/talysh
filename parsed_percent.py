import nltk
d = open('C:\\Users\\User\\Desktop\\corpus\\parsed.txt', 'r', encoding='utf8')
f = open('C:\\Users\\User\\Desktop\\corpus\\priorities.txt', 'r', encoding='utf8')
d = d.readlines()
f = f.readlines()
a = 0
b = 0

for line in d:
    x = nltk.word_tokenize(line)
    a = a + int(x[1])

for line in f:
    y = nltk.word_tokenize(line)
    b = b + int(y[1])
c = a + b
i = c / 100
w = a / i
print(c)
print(w)

