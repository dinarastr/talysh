import nltk
import re
f = open('C:\\Users\\User\\Desktop\\corpus\\test.txt', 'r', encoding='utf8')
verbs = open('C:\\Users\\User\\Desktop\\corpus\\noun_lex.txt', 'w', encoding='utf8')
for line in f:
    if 'N' in line:
        x = nltk.word_tokenize(line)
        y = ' '.join(x[2:])
        verbs.write('-lexeme'+'\n')
        verbs.write(' lex: '+x[1]+'\n')
        if x[1][-1] in 'aeiıəo':
            verbs.write(' stem: '+x[1][:-1]+'.|'+x[1]+'.\n')
        else:
            verbs.write(' stem: '+x[1]+'.\n')
        verbs.write(' gram: N'+'\n')
        if x[1][-1] in 'aeiıəo':
            verbs.write(' paradigm: N_vow'+'\n')
        else:
            verbs.write(' paradigm: N_cons'+'\n')
        verbs.write(' trans_ru: '+y+'\n')
        verbs.write('\n')
    elif 'ADV' in line:
        x = nltk.word_tokenize(line)
        y = ' '.join(x[2:])
        verbs.write('-lexeme'+'\n')
        verbs.write(' lex: '+x[1]+'\n')
        verbs.write(' stem: '+x[1]+'\n')
        verbs.write(' gram: ADV'+'\n')
        verbs.write(' paradigm: ADV'+'\n')
        verbs.write(' trans_ru: '+y+'\n')
        verbs.write('\n')
    elif 'CONJ' in line:
        x = nltk.word_tokenize(line)
        y = ' '.join(x[2:])
        verbs.write('-lexeme'+'\n')
        verbs.write(' lex: '+x[1]+'\n')
        verbs.write(' stem: '+x[1]+'\n')
        verbs.write(' gram: CONJ'+'\n')
        verbs.write(' paradigm: CONJ'+'\n')
        verbs.write(' trans_ru: '+y+'\n')
        verbs.write('\n')
    elif 'ADP' in line:
        x = nltk.word_tokenize(line)
        y = ' '.join(x[2:])
        verbs.write('-lexeme'+'\n')
        verbs.write(' lex: '+x[1]+'\n')
        verbs.write(' stem: '+x[1]+'\n')
        verbs.write(' gram: ADP'+'\n')
        verbs.write(' paradigm: ADP'+'\n')
        verbs.write(' trans_ru: '+y+'\n')
        verbs.write('\n')
    elif 'PRO' in line:
        x = nltk.word_tokenize(line)
        y = ' '.join(x[2:])
        verbs.write('-lexeme'+'\n')
        verbs.write(' lex: '+x[1]+'\n')
        verbs.write(' stem: '+x[1]+'\n')
        verbs.write(' gram: PRO'+'\n')
        verbs.write(' paradigm: PRO'+'\n')
        verbs.write(' trans_ru: '+y+'\n')
        verbs.write('\n')
    elif 'INTJ' in line:
        x = nltk.word_tokenize(line)
        y = ' '.join(x[2:])
        verbs.write('-lexeme'+'\n')
        verbs.write(' lex: '+x[1]+'\n')
        verbs.write(' stem: '+x[1]+'\n')
        verbs.write(' gram: INTJ'+'\n')
        verbs.write(' paradigm: INTJ'+'\n')
        verbs.write(' trans_ru: '+y+'\n')
        verbs.write('\n')
verbs.close()




