## 1 - K-Means Clustering algorithm
Tags: Machine Learning<br>
K-Means clustering is an unsupervised learning technique. This can be used when unlabeled data is available.

Steps:
1. Pick K random points from the dataset as initial cluster centroids
2. Find distance of each point in the dataset to each of the K centroids and assign the point to the cluster of the nearest centroid
3. Compute new centroid for each cluster
4. Repeat steps 2 and 3 until none of the centroids change

[Reference](https://mubaris.com/posts/kmeans-clustering/) | [Python implementation](https://github.com/ppai22/k-means-clustering-python)

## 2 - Dataframe from dictionary
Tags: Pandas<br>
Use of pandas module to create a dataframe directly from a dictionary
```python
data = {'Country': ['India', 'Australia', 'England', 'South Africa'],
        'Bowler': ['Bumrah', 'Cummins', 'Archer', 'Rabada']}
df = pandas.DataFrame.from_dict(data)
```
Yes, I am a cricket geek.

## 3 - Copy columns from one dataframe to new dataframe
Tags: Pandas<br>
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

## 4 - Drop columns from a dataframe
Tags: Pandas<br>
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

## 5 - Access columns using column names
Tags: Pandas<br>
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

## 6 - Fetching unique elements from a column
Tags: Pandas<br>
Making use of data frame from above article:
```python
>>> df.India.unique()
array(['Delhi', 'Mumbai', 'Bengaluru'], dtype=object)
```

## 6 - Sort Dataframe by column values
Tags: Pandas<br>
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

## 7 - re.match()
Tags: Regular Expressions<br>
re.match() matches only if the pattern exists at the beginning of the string
```python
>>> str1 = 'I love Python'
>>> re.match('python', str1.lower())
None
>>> str2 = 'Python programming language'
>>> re.match('python', str2.lower())
<re.Match object; span=(0, 6), match='python'>
```

## 8 - re.search()
Tags: Regular Expressions<br>
re.search() matches if the pattern exists anywhere in the string
```python
>>> str1 = 'I love Python'
>>> re.search('python', str1.lower())
<re.Match object; span=(7, 13), match='python'>
>>> str2 = 'Python programming language'
>>> re.search('python', str.lower())
<re.Match object; span=(0, 6), match='python'>
```

## 9 - re.findall()
Tags: Regular Expressions<br>
re.findall() finds all non-overlapping matches
```python
>>> str = 'LOLOLOL'
>>> matches = [match for match in re.findall('LOL', str)]
>>> matches
['LOL', 'LOL']
```
re.findall has found the first LOL and the last LOL and missed the overlapping middle LOL

## 10 - re.findall() to find overlapping matches
Tags: Regular Expressions<br>
A lookaround is used to find overlapping matches using re.findall()
```python
>>> str = 'LOLOLOL'
>>> matches = [match for match in re.findall('(?=(LOL))', str)]
>>> matches
['LOL', 'LOL', 'LOL']
```
[Reference](https://stackoverflow.com/questions/11430863/how-to-find-overlapping-matches-with-a-regexp)

## 11 - re.sub()
Tags: Regular Expressions<br>
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
