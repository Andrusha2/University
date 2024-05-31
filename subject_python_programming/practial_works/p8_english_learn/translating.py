import translate


def to_en(final_dict):
    translator = translate.Translator(from_lang='ru', to_lang='en')
    for i in range(len(final_dict)):
        final_dict[i].insert(1, translator.translate(final_dict[i][0]).lower())
    return final_dict
