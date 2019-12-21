## 1 - re.match()

re.match() matches only if the pattern exists at the beginning of the string
```python
>>> str1 = 'I love Python'
>>> re.match('python', str1.lower())
None
>>> str2 = 'Python programming language'
>>> re.match('python', str2.lower())
<re.Match object; span=(0, 6), match='python'>
```

## 2 - re.search()

re.search() matches if the pattern exists anywhere in the string
```python
>>> str1 = 'I love Python'
>>> re.search('python', str1.lower())
<re.Match object; span=(7, 13), match='python'>
>>> str2 = 'Python programming language'
>>> re.search('python', str.lower())
<re.Match object; span=(0, 6), match='python'>
```

## 3 - re.findall()

re.findall() finds all non-overlapping matches
```python
>>> str = 'LOLOLOL'
>>> matches = [match for match in re.findall('LOL', str)]
>>> matches
['LOL', 'LOL']
```
re.findall has found the first LOL and the last LOL and missed the overlapping middle LOL

## 4 - re.findall() to find overlapping matches

A lookaround is used to find overlapping matches using re.findall()
```python
>>> str = 'LOLOLOL'
>>> matches = [match for match in re.findall('(?=(LOL))', str)]
>>> matches
['LOL', 'LOL', 'LOL']
```
[Reference](https://stackoverflow.com/questions/11430863/how-to-find-overlapping-matches-with-a-regexp)

## 5 - re.sub()

re.sub() is used to substitute a particular pattern with another string
```python
re.sub(pattern, replacement_string, string)
```
Statement to replace all '-'s in the string with '*'s
```python
>>> s = 'A-B-C-D-E-F-G-H'
>>> re.sub('-', '*', s)
'A*B*C*D*E*F*G*H'
```
re.sub() can also be used with 'count=n' parameter to substitute the first n instances only
```python
>>> s = 'A-B-C-D-E-F-G-H'
>>> re.sub('-', '*', s, count=3)
'A*B*C*D-E-F-G-H'
```
Expression needs to be stored in another variable to access the substituted string again.
