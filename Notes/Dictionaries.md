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
