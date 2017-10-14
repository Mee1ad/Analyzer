import re
import error as e

data_type = {'int': r'^[0-9]$',
             'float': r'^[0-9].?[0-9]*',
             'string': r'^(\").*(\")$'}


def type_check(word):
    word_list = []
    for i in word:
        word_list.append(word[i])
    # print(word_list)
    for i in range(len(word_list)):

        for type in data_type:
            if word_list[i] == type:
                if word_list[i + 2] == '=':
                    if not re.match(data_type[type], word_list[i + 3]):
                        print(e.bred, e.fblue, 'Type Error : Value Of', type, 'is incorrect')



                        # if word_list[i] == 'int':
                        #    if word_list[i + 2] == '=':
                        #        if not re.match(data_type['int'], word_list[i + 3]):
                        #            print(e.bred, e.fblue, 'Type Error : Value Of int is incorrect')

                        # if word_list[i] == 'float':
                        #    if word_list[i + 2] == '=':
                        #        if not re.match(data_type['float'], word_list[i + 3]):
                        #            print(e.bred, e.fblue, 'Type Error : Value Of float is incorrect')

                        # if word_list[i] == 'string':
                        #    if word_list[i + 2] == '=':
                        #        if not re.match(data_type['string'], word_list[i + 3]):
                        #            print(e.bred, e.fblue, 'Type Error : Value Of string is incorrect')
