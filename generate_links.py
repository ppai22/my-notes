import re
import os


notes = list()
for root, dirs, files in os.walk(r'.\Notes'):
    for file in files:
        if file.split('.')[-1] == 'md':
            with open('.\\Notes\\' + file, 'r+') as md:
                md_lines = md.readlines()
                for line in md_lines:
                    if re.match(r'##\s', line):
                        notes.append((line.split('## ')[-1].strip('\n'), root + '\\' + file))

with open(r'.\README.md', 'w+') as readme:
    readme.write('# My personal notes on Python\n\n')
    readme.write('|LINKS|\n')
    readme.write('|------|\n')
    for note in notes:
        readme.write('|' + '[' + note[0] + ']' + '(' + note[1] + ')' + '|' + '\n')
