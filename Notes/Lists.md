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
This method only works for level 1 of sub-lists.<br>
So, if ```li = [[1, 2], [3, 4, 5], [6, 7]]```, then ```flat_list = [1, 2, 3, 4, 5, 6, 7]```<br>
But if ```li = [[1, 2], [3, [4, 5]], [6, 7]]```, then ```flat_list = [1, 2, 3, [4, 5], 6, 7]```<br>
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

## 4 - Sort a list of tuples by value

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
