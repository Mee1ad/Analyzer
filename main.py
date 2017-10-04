import dataset
import re
import lexical_analyzer as la
import syntax_analyzer as sa
import error

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

words = la.split()
la.regex(words)
sa.statement_syntax(text)
error.syntax(words)
