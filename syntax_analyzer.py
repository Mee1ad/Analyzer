import re


def check_syntax(text):
    if_pattern = r'if\(.+\)(\n)*{(\n)?.+(\n)?}'
    while_pattern = r'while\(.+\)(\n)*{(\n)?.+(\n)?}'
    for_pattern = r'for\((.+=.+);(.+[\<\>]\=?.+);(.+);?\)(\n)*{(\n)?.+(\n)?}'

    if 'if' in text:
        if re.search(if_pattern, text):
            print("ok")
        else:
            print('<< if >> syntax is wrong')

    if 'while' in text:
        if re.search(while_pattern, text):
            print("ok")
        else:
            print('<< if >> syntax is wrong')

    if 'for' in text:
        if re.search(if_pattern, text):
            print("ok")
        else:
            print('<< if >> syntax is wrong')
