## 1 - Dataframe from dictionary

Use of pandas module to create a dataframe directly from a dictionary
```python
data = {'Country': ['India', 'Australia', 'England', 'South Africa'],
        'Bowler': ['Bumrah', 'Cummins', 'Archer', 'Rabada']}
df = pandas.DataFrame.from_dict(data)
```
Yes, I am a cricket geek.

## 2 - Copy columns from one dataframe to new dataframe

```python
data = {'Man Utd': ['Rashford', 'Martial', 'James'],
        'Man City': ['Sterling', 'Aguero', 'Silva'],
        'Liverpool': ['Mane', 'Firmino', 'Salah'],
        'Tottenham': ['Son', 'Kane', 'Alli']}
old = pd.DataFrame.from_dict(data)
```
To copy only the columns relevant to the Manchester clubs to a new dataframe:
```python
new = old[['Man Utd', 'Man City']].copy()
```
Yes, I love football too.

## 3 - Drop columns from a dataframe

```python
data = {'Man Utd': ['Rashford', 'Martial', 'James'],
        'Man City': ['Sterling', 'Aguero', 'Silva'],
        'Liverpool': ['Mane', 'Firmino', 'Salah'],
        'Tottenham': ['Son', 'Kane', 'Alli']}
old = pd.DataFrame.from_dict(data)
```
Drop columns of clubs from Manchester:
```python
new = old.drop(['Man Utd', 'Man City'], axis=1)
```
```axis=1``` means drop columns. ```axis=0``` is the default which means drop rows.<br>
Another way to specify to drop columns is
```python
new = old.drop(columns=['Man Utd', 'Man City'])
```

## 4 - Access columns using column names

Dataframe used:
```python
>>> dataset = {'India': ['Delhi', 'Mumbai', 'Bengaluru', 'Mumbai'],
          'Australia': ['Melbourne', 'Sydney', 'Brisbane', 'Perth'],
          'South Africa': ['Pretoria', 'Cape Town', 'Durban', 'Bloemfontein']}
>>> df = pd.DataFrame(dataset)
```

```python
>>> df['India']
0        Delhi
1       Mumbai
2    Bengaluru
3       Mumbai
```

```python
>>> df.India
0        Delhi
1       Mumbai
2    Bengaluru
3       Mumbai
```

## 5 - Fetching unique elements from a column

Making use of data frame from above article:
```python
>>> df.India.unique()
array(['Delhi', 'Mumbai', 'Bengaluru'], dtype=object)
```

## 6 - Sort Dataframe by column values

```python
pl_dict = {'Man Utd': [3, 1, 1, 10], 'Man City': [4, 0, 1, 12], 'Arsenal': [2, 0, 3, 6], 'Chelsea': [1, 3, 2, 6]}
df = pandas.DataFrame(pl_dict, columns=['Wins', 'Draws', 'Losses', 'Points'])
```
To sort the teams by points:
```python
df = df.sort_values(by='Points')
```
To sort the teams based on points and then by wins if there is a tie:
```python
df = df.sort_values(by=['Points', 'Wins'])
```
[Reference](https://thispointer.com/pandas-sort-rows-or-columns-in-dataframe-based-on-values-using-dataframe-sort_values/)

## 7 - Dataframe to Numpy array

```python
import pandas as pd
dataframe = pd.DataFrame({"a": [1, 2, 3, 4], "b": [5, 6, 7, 8], "c": [9, 10, 11, 12]})
np_arr = dataframe.to_numpy()
print(dataframe)
print(np_arr)
```

The output to the above code is:
```python
dataframe:
   a  b   c
0  1  5   9
1  2  6  10
2  3  7  11
3  4  8  12
```
```python
np_arr:
[[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]
```

This method is extremely useful if you have read a dataset from a csv file using pandas and then want to pass the input parameters to a Tensorflow model as a numpy array.
