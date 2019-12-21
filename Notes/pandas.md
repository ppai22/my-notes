## 1 - Dataframe from dictionary

Use of pandas module to create a dataframe directly from a dictionary
```python
data = {'Country': ['India', 'Australia', 'England', 'South Africa'],
        'Bowler': ['Bumrah', 'Cummins', 'Archer', 'Rabada']}
df = pandas.DataFrame.from_dict(data)
```
Yes, I am a cricket geek.

# 2 - Copy columns from one dataframe to new dataframe

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

# 3 - Drop columns from a dataframe

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
