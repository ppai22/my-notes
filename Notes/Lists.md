## 1 - List Comprehensions

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

## 2 - Flatten a list of lists

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
[Reference](https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists)

## 3 - Reverse a list

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
