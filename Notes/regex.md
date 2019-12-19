## 1 - re.match()

##### re.match() matches only if the pattern exists at the beginning of the string
```python
>>> str1 = 'I love Python'
>>> re.match('python', str1.lower())
None
>>> str2 = 'Python programming language'
>>> re.match('python', str2.lower())
<re.Match object; span=(0, 6), match='python'>
```

## 2 - re.search()

##### re.search() matches if the pattern exists anywhere in the string
```python
>>> str1 = 'I love Python'
>>> re.search('python', str1.lower())
<re.Match object; span=(7, 13), match='python'>
>>> str2 = 'Python programming language'
>>> re.search('python', str.lower())
<re.Match object; span=(0, 6), match='python'>
```
