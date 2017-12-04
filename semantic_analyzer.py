import re
import error as e

data_type = {'int': r'^[0-9]+$',
             'float': r'^[0-9].?[0-9]*',
             'string': r'^(\").*(\")$'}


def type_check(words, values):
    word_list = []
    for i in words:
        word_list.append(words[i])
    for i in range(len(word_list)):
        for type in data_type:
            if word_list[i] == type:
                try:
                    if word_list[i + 2] == '=':
                        if not re.match(data_type[type], word_list[i + 3]):
                            print(e.bred, e.fblue, 'Type Error : Value Of', type, 'is incorrect')
                except Exception:
                    print('semantic eception', Exception)

    value_type = {}
    for key in values:
        if values[key] in value_type:
            if value_type[values[key]] != values[key]:
                print('ValueError:', values[key], 'is not', key[0])
        value_type[key[1]] = key[0]
        value_type[values[key]] = key[0]

