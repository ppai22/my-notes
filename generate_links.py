import re
import os


repo = r'https://github.com/ppai22/my-notes/blob/master/Notes/'
notes = list()
for root, dirs, files in os.walk(r'.\Notes'):
    for file in files:
        if file.split('.')[-1] == 'md':
            with open('.\\Notes\\' + file, 'r+') as md:
                md_lines = md.readlines()
                for line in md_lines:
                    if re.match(r'##\s', line):
                        note_title = line.split('## ')[-1].strip('\n')
                        note_link = re.sub(' ', '-', note_title.lower())
                        notes.append((note_title, repo + file + '#' + note_link))

with open(r'.\README.md', 'w+') as readme:
    readme.write('# My personal notes on Python\n\n')
    readme.write('|LINKS|\n')
    readme.write('|------|\n')
    for note in notes:
        readme.write('|' + '[' + note[0] + ']' + '(' + note[1] + ')' + '|' + '\n')
