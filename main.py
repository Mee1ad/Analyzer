import dataset
import re
import regex as reg
from error import syntax

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

words = reg.split()
reg.regex(words)
reg.print_m()


syntax(words)