import re

if_pattern = r'if\(.+\)(\n)*{(\n)?.+(\n)?}'
while_pattern = r'while\(.+\)(\n)*{(\n)?.+(\n)?}'
for_pattern = r'for\((.+=.+);(.+[\<\>]\=?.+);(.+);?\)(\n)*{(\n)?.+(\n)?}'
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
