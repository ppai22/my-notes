import re
import os


repo = r'https://github.com/ppai22/my-notes/blob/master/Notes/'
categories = dict()
for root, dirs, files in os.walk(r'.\Notes'):
    for file in files:
        if file.split('.')[-1] == 'md':
            name = file.split('.')[0]
            notes = list()
            with open('.\\Notes\\' + file, 'r+') as md:
                md_lines = md.readlines()
                for line in md_lines:
                    if re.match(r'##\s', line):
                        note_title = line.split('## ')[-1].strip('\n')
                        note_link = re.sub(' ', '-', note_title.lower())
                        note_link = re.sub('[.()]', '', note_link.lower())
                        notes.append((note_title, repo + file + '#' + note_link))
            categories[name] = notes

with open(r'.\README.md', 'w+') as readme:
    readme.write('# My personal notes on Python\n\n')
    readme.write('|LINKS|\n')
    readme.write('|------|\n')
    for category in categories.keys():
        readme.write('|' + '**' + category + '**' + '|' + '\n')
        readme.write('|' + '<ul>')
        for note in categories[category]:
            readme.write('<li>' + '[' + note[0] + ']' + '(' + note[1] + ')' + '</li>')
        readme.write('</ul>' + '|' + '\n')
