## 1 - List Comprehensions

##### For loop that generates list of first five numbers
```
li = []
for i in range(1, 6):
	li.append(i)

# li = [1, 2, 3, 4, 5]
```
##### List comprehension to do the same
```
li = [i for i in range(1, 6)]
```

## 2 - Flatten a list of lists

```
flat_list = []
for sub_list in li:
	for item in sub_list:
		flat_list.append(item)
```
##### This is the same as
```
flat_list = [item for sub_list in li for item in sub_list]
```
