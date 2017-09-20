import re

bred = '\033[101m'
fblue = '\033[94m'


class syntax:
    def __init__(self, words):
        word = list(words.values())
        print('\n')
        self.word = word
        self.end_of_line(words)
        self.bracket(words)

    def end_of_line(self, words):
        with open("code.txt", "r") as file:
            text = file.read()
            sep_line = text.split('\n')
            error_pattern = r'[;){]'
            for i in range(len(sep_line)):
                try:
                    if not re.match(error_pattern, sep_line[i][-1:]):
                        if sep_line[i][-1:] == '}':
                            if sep_line[i][-2:-1] != ';' and sep_line[i][-2:-1] != ')':
                                if sep_line[i] != '}':
                                    print(bred, fblue, "Syntax Error : Exepted ';' in line", i + 1)
                        elif 'if' in self.word or 'while' in self.word or 'for' in self.word:
                            if '(' in self.word and ')' not in self.word:
                                pass
                            else:
                                print(bred, fblue, "Syntax Error : Exepted ';' in line", i + 1)

                        else:
                            print(bred, fblue, "Syntax Error : Exepted ';' in line", i + 1)
                except:
                    continue

    def bracket(self, words):
        if '(' in self.word:
            if ')' not in self.word:
                print(bred, fblue, 'Syntax Error : an ")" excepted')
        if '{' in self.word:
            if '}' not in self.word:
                print(bred, fblue, 'Syntax Error : an "}" excepted')
        if ')' in self.word:
            if '(' not in self.word:
                print(bred, fblue, 'Syntax Error : an "(" excepted')
        if '}' in self.word:
            if '{' not in self.word:
                print(bred, fblue, 'Syntax Error : an "{" excepted')
