import pymorphy3


def to_normal(filename):
    f = open(filename, encoding='utf-8')
    word_l = f.read().splitlines()
    final_word_l = list()
    morph = pymorphy3.MorphAnalyzer()
    for i in word_l:
        word = ''
        for j in i:
            if j.isalpha():
                word += j
            else:
                if word == '':
                    pass
                else:
                    final_word_l.append(morph.parse(word.lower())[0].normal_form)
                    word = ''
    return final_word_l


