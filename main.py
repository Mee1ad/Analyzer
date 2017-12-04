import dataset
import re
import lexical_analyzer as la
import syntax_analyzer as sya
import error
import semantic_analyzer as sea

a = '\033[35m'

print(a + 'Enter Your Code here!\n')
with open("code.txt", "w+") as file:
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    file.write(text)

try:
    words = la.split()
    values = la.regex(words)
    # print('2')
    sya.statement_syntax(text)
    # print('3')
    error.syntax(words)
    # print('4')
    sea.type_check(words, values)
    # print('5')
except Exception as e:
    print('main exception')
    raise e
