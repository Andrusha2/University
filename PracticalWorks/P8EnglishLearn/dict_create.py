def to_dict(final_word_l):
    dictionary = dict()
    for i in final_word_l:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    final_dict = [list(s) for s in dictionary.items()]
    final_dict.sort(key=lambda x: x[1], reverse=True)
    return final_dict