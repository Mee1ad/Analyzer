import re
import dataset


def split():
    with open("code.txt", "r") as file:
        global text
        text = file.read()
        text2 = text
        global word
        word = re.findall(r'(\"?\w+\.?\w*\"?)', text)
        # print('word=', word)
        op = re.findall(r'[\+\-\*\{\}\(\)\];]', text)
        rop = re.findall(r'[\=\<\>\!]=?', text)
        token = word + op + rop
        len_token = len(token)
        token_pos = []
        for i in range(len_token):
            # if text2.index('if'):
            # if text2.index(token[i]) in token_pos:
            # text_to_be_replace = text2[:text2.index(token[i]) + 1]
            # replaced_text = replace(text_to_be_replace, token[i])
            # replaced_text += text2[text2.index(token[i]) + 1:]
            # text2 = replaced_text
            token_pos.append(text2.index(token[i]))
            text2 = replace(text2, token[i])
        # print('token_pos', token_pos, '\n')
        # print('token: ', token, '\n')3
        token_dict = {}
        for i in range(len_token):
            token_dict[token_pos[i]] = token[i]
        # print(sorted(token_dict))
        token_key = sorted(token_dict)
        sorted_token = {}
        for i in range(len(token_dict)):
            sorted_token[token_key[i]] = token_dict[token_key[i]]
        return sorted_token


def replace(text, word):
    len_word = len(word)
    r = ''
    for i in range(len_word):
        r += '^'
    if text.index(word) != text.rindex(word):
        text2 = text[:text.index(word) + 1]
        text2 = text2.replace(word, r)
        text2 += text[text.index(word) + 1:]
        return text2
    else:
        text = text.replace(word, r)
        return text


def regex(dic):
    db = dataset.connect('sqlite:///analyzer.db')
    table = db['result']
    table.delete()
    token_name = {
        '': r'(^int$)',
        ' ': r'(^float$)',
        '  ': r'(^string$)',
        '   ': r'(^if$)',
        '    ': r'(^while$)',
        '     ': r'(^for$)',
        'string': r'^".*"$',
        'output': r'print',
        'ident': r'^[a-zA-Z_][a-zA-Z0-9_]*',
        'illegal_ident': r'^[0-9]+[a-zA-Z_]+',
        'float-number': r'[0-9]+\.[0-9]*$',
        'number': r'^[0-9]+[0-9]*$',
        'r-operator': r'[\=<>!]=',
        'operator': r'[\*/+=-]',
        'open-paarnthes': r'\(',
        'close-paarnthes': r'\)',
        'open-curlybrucket': r'\{',
        'close-curlybrucket': r'\}',
        'end of line': r';'
    }
    global pattern
    l = list(dic.keys())
    for k in dic:
        for pattern in token_name:
            if re.match(token_name[pattern], dic[k]):
                val = ''
                if pattern == 'ident':
                    i = text.index(dic[k])
                    if i not in l:
                        i = text.rindex(dic[k])
                    p = l.index(i)
                    print(l , p  , ' - ' , dic[l[p]])

                    if dic[l[p+1]] == '=':
                        print('yeees' , dic[l[p]])
                        j = word.index(dic[k])
                        val = word[j + 1]
                table.insert(dict(token=dic[k], type=pattern, value=val, position=k))
                break


def print_m():
    if 'print' in word:
        i = word.index('print')
        print('\n' + word[i + 1])
