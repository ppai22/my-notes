## 1 - OrderedDict
Tags: Dictionaries<br>
Python dictionaries are unordered i.e. they do not remember the way in which keys are initialized.
The collections module has a dictionary sub-class OrderedDict() that remembers the order in which keys were initialized.
```python
from collections import OrderedDict
d = OrderedDict()
d['India'] = 'Virat Kohli'
d['Australia'] = 'Steve Smith'
d['New Zealandd'] = 'Kane Williamson'
```
From Python 3.7, dictionaries in python are ordered [Reference](https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6)

## 2 - Dictionary comprehensions
Tags: Dictionaries<br>
Similar to list comprehensions, dictionary comprehensions allow initializing new dictionary with a single line of code by avoiding for loops
```python
>>> dict_1 = {'A': 1, 'B': 2, 'C': 3}
>>> dict_1.items()
dict_items([('A', 1), ('B', 2), ('C', 3)])
>>> new_dict = {key:val**2 for (key,val) in dict_1.items()}
>>> new_dict
{'A': 1, 'B': 4, 'C': 9}
```

## 3 - Write/Read data to/from a JSON file
Tags: JSON<br>
```python
import json
```
Write:
```python
data = {'One': 1, 'Two': 2, 'Three': 3}
with open('data.json', 'w+') as f:
    json.dump(data, f)
```
Read:
```python
with open('data.json', 'r+') as f:
    data = json.load(f)
```

## 4 - Accessing key,value pairs
Tags: Dictionaries<br>
```python
dict_1 = {'a': 1, 'b': 2, 'c': 3}
for key in dict_1:
    print(key, dict_1[key])
```
is the same as
```python
for key, value in dict_1.items():
    print(key, value)
```

## 5 - List Comprehensions
Tags: Lists<br>
For loop that generates list of first five numbers
```python
li = []
for i in range(1, 6):
	li.append(i)

# li = [1, 2, 3, 4, 5]
```
List comprehension to do the same
```python
li = [i for i in range(1, 6)]
```

## 6 - Flatten a list of lists
Tags: Lists<br>
```python
flat_list = []
for sub_list in li:
	for item in sub_list:
		flat_list.append(item)
```
This is the same as
```python
flat_list = [item for sub_list in li for item in sub_list]
```
This method only works for level 1 of sub-lists.<br>
So, if ```li = [[1, 2], [3, 4, 5], [6, 7]]```, then ```flat_list = [1, 2, 3, 4, 5, 6, 7]```<br>
But if ```li = [[1, 2], [3, [4, 5]], [6, 7]]```, then ```flat_list = [1, 2, 3, [4, 5], 6, 7]```<br>
[Reference](https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists)


## 7 - Reverse a list
Tags: Lists<br>
There are 3 methods to reverse a list in python

##### Method 1: Use of reverse()
reverse() just reverses the list in-place
```python
>>> li = [1, 2, 3, 4, 5]
>>> li.reverse()
>>> li
[5, 4, 3, 2, 1]
```

##### Method 2: Use of reversed()
reversed() returns an iterator that accesses the list in reverse order
```python
>>> li = [1, 2, 3, 4, 5]
>>> [item for item in reverses(li)]
[5, 4, 3, 2, 1]
```

##### Method 3: Use of list slicing
```python
>>> li = [1, 2, 3, 4, 5]
>>> li[::-1]
[5, 4, 3, 2, 1]
```

## 8 - Sort a list of tuples by value
Tags: Lists<br>
The aim is to sort a list of tuples by the first value of the tuple

##### Method 1: Using lambda function
```python
>>> li = [(3, 'c'), (5, 'e'), (2, 'b'), (1, 'a'), (4, 'd')]
>>> sorted(li, key=lambda x: x[0])
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
```

##### Method 2: Using operator.itemgetter
```python
>>> from operator import itemgetter
>>> li = [(3, 'c'), (5, 'e'), (2, 'b'), (1, 'a'), (4, 'd')]
>>> sorted(li, key=itemgetter(0))
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
```

To sort in reverse order, use ```reverse=True``` as a parameter<br>
To sort inplace, use ```li.sort(<itemgetter/lambda>)```<br>
[Reference](https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value)

## 9 - if-else inside a List Comprehension
Tags: Lists<br>
```python
li = [1, 2, 3, 4, 5, 6]
output =[]
for i in li:
    if i%2 == 0:
        output.append((i, 'EVEN'))
    else:
        output.append((i,'ODD'))
print(output)
```
The above code would give:
```python
[(1, 'ODD'), (2, 'EVEN'), (3, 'ODD'), (4, 'EVEN'), (5, 'ODD'), (6, 'EVEN')]
```
The same could be achieved using a simple list comprehension as shown below:
```python
output = [(i, 'EVEN') if i%2 == 0 else (i, 'ODD') for i in li]
```
[Reference](https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension)

## 6 - Index of element in a list
Tags: Lists<br>
```python
>>> li = ['V Kohli', 'S Smith', 'K Williamson', 'D Warner', 'J Root', 'B Azam']
>>> li.index('S Smith')
1
```

```python
>>> li = [[9, 0, 3], [3, 8, 2], [5, 6, 0], [7, 2, 9], [4, 2, 9]]
>>> li.index([5, 6, 0])
2
```

## 10 - Sum of second values in list of tuples
Tags: Lists<br>
```python
>>> li = [('Kohli', 10), ('Smith', 4), ('Warner', 9), ('Williamson', 9)]
>>> sum(ducks for name, ducks in li)
32
```
[Reference](https://stackoverflow.com/questions/12218112/sum-the-second-value-of-each-tuple-in-a-list)

## 8 - Unpacking lists to formatted strings
Tags: Lists, Strings<br>
```python
import datetime

y, m, d = str(datetime.datetime.now().date()).split('-')
print(f"{d}/{m}/{y}")
```
`Output: 06/02/2020`

## 11 - Splitting strings in Python
Tags: Lists, Strings<br>
The `split()` function can be used to split strings in python into a list.

```python
>>> str = 'one two three four five'
>>> print(str.split())
['one', 'two', 'three', 'four', 'five']
>>> print(type(str.split()))
<class 'list'>
```

Splitting of strings can be done based on delimiter
```python
>>> str_dashed = 'one-two-three-four-five'
>>> print(str_dashed.split('-'))
['one', 'two', 'three', 'four', 'five']
```

split() also can take a parameter maxsplit to split string into certain number of splits
```python
>>> print(str.split(' ', 2)) #maxsplit=2
['one', 'two', 'three four five']
```

To split from the right side, `rsplit()` can be used
```python
>>> print(str.rsplit(' ', 2))
['one two three', 'four', 'five']
```

To split strings based on '\n' characters, `split()` or `splitlines()` could be used
```python
>>> str_lines = 'one\ntwo\nthree\nfour\nfive'
>>> print(str_lines.split())
['one', 'two', 'three', 'four', 'five']
>>> print(str_lines.split('\n'))
['one', 'two', 'three', 'four', 'five']
>>> print(str_lines.splitlines())
['one', 'two', 'three', 'four', 'five']
```

split() recognises both newline and space when no seperator is explicitly mentioned
```python
>>> str_mixed = 'one two\nthree four'
['one', 'two', 'three', 'four']
```

To join these split strings back join() method is used
```python
>>> li = ['one', 'two', 'three', 'four', 'five']
>>> '***'.join(li)
'one***two***three***four***five'
```

Splitting based on regular expressions acn be done using split() from re module
```python
>>> import re
>>> str_reg = 'one-two*three+four#five'
>>> print(re.split('[-*+#]', str_reg))
['one', 'two', 'three', 'four', 'five']
```

[Reference](https://note.nkmk.me/en/python-split-rsplit-splitlines-re/)
