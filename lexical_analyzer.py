import re
import dataset


def split():
    with open("code.txt", "r") as file:
        global text
        text = file.read()
        text2 = text
        global word
        word = re.findall(r'(\"?\w+\.?\w*\"?)', text)
        op = re.findall(r'[\+\-\*\{\}\(\)\];]', text)
        rop = re.findall(r'[\=\<\>\!]=?', text)
        token = word + op + rop
        len_token = len(token)
        token_pos = []
        for i in range(len_token):
            token_pos.append(text2.index(token[i]))
            text2 = replace(text2, token[i])
        token_dict = {}
        for i in range(len_token):
            token_dict[token_pos[i]] = token[i]
        # print(sorted(token_dict))
        token_key = sorted(token_dict)
        global word_dict
        word_dict = {}
        for i in range(len(token_dict)):
            word_dict[token_key[i]] = token_dict[token_key[i]]

        return word_dict


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
    # print(l)
    for k in dic:
        for pattern in token_name:
            if re.match(token_name[pattern], dic[k]):
                val = ''
                if pattern == 'ident':
                    i = text.index(dic[k])
                    #print('i is:', i)
                    if i not in l:
                        i = text.rindex(dic[k])
                        # print('rindex i:', i)
                    #print('dic[i]', dic[i])
                    p = l.index(i)
                    # print(l , p  , ' - ' , dic[l[p]])
                    try:
                        if dic[l[p + 1]] == '=':
                            # print('yeees' , dic[l[p]])
                            j = word.index(dic[k])
                            val = word[j + 1]
                    except:
                        pass
                table.insert(dict(token=dic[k], type=pattern, value=val, position=k))
                break

