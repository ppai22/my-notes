## 1 - OrderedDict

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

Similar to list comprehensions, dictionary comprehensions allow initializing new dictionary with a single line of code by avoiding for loops
```python
>>> dict_1 = {'A': 1, 'B': 2, 'C': 3}
>>> dict_1.items()
dict_items([('A', 1), ('B', 2), ('C', 3)])
>>> new_dict = {key:val**2 for (key,val) in dict_1.items()}
>>> new_dict
{'A': 1, 'B': 4, 'C': 9}
```