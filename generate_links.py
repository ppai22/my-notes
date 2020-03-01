import re
import os


repo = r'https://github.com/ppai22/my-notes/blob/reformat/Notes/'
articles = dict()
for root, dirs, files in os.walk(r'.\Notes'):
    for file in files:
        if file.split('.')[-1] == 'md':
            name = file.split('.')[0]
            notes = list()
            with open('.\\Notes\\' + file, 'r+') as md:
                md_lines = md.readlines()
                for line in range(len(md_lines)):
                    if re.match(r'##\s', md_lines[line]):
                        note_title = md_lines[line].split('## ')[-1].strip('\n')
                        note_link = re.sub(' ', '-', note_title.lower())
                        note_link = re.sub('[.()/,]', '', note_link.lower())
                        if re.match(r'Tags:', md_lines[line+1]):
                            tags = md_lines[line+1].split('Tags:')[-1].strip().strip('\n').split('<br>')[0]
                        else:
                            tags = []
                        notes.append((note_title, repo + file + '#' + note_link, tags))
            articles[name] = notes
print(articles)


with open(r'.\README.md', 'w+') as readme:
    readme.write('# My personal notes on Python\n\n')
    readme.write('|LINKS|\n')
    readme.write('|------|\n')
    for name in articles.keys():
        readme.write('|' + '**' + name + '**' + '|' + '\n')
        readme.write('|' + '<ul>')
        for note in articles[name]:
            readme.write('<li>' + '[' + note[0] + ']' + '(' + note[1] + ')' + '</li>')
        readme.write('</ul>' + '|' + '\n')
