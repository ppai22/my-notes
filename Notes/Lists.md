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

## 5 - if-else inside a List Comprehension

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

## 7 - Sum of second values in list of tuples

```python
>>> li = [('Kohli', 10), ('Smith', 4), ('Warner', 9), ('Williamson', 9)]
>>> sum(ducks for name, ducks in li)
32
```
[Reference](https://stackoverflow.com/questions/12218112/sum-the-second-value-of-each-tuple-in-a-list)

## 8 - Unpacking lists to formatted strings

```python
import datetime

y, m, d = str(datetime.datetime.now().date()).split('-')
print(f"{d}/{m}/{y}")
```
`Output: 06/02/2020`
