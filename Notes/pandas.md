## 1 - Dataframe from dictionary

###### Use of pandas module to create a dataframe directly from a dictionary
```python
dict = {'Country': ['India', 'Australia', 'England', 'South Africa'],
        'Bowler': ['Bumrah', 'Cummins', 'Archer', 'Rabada']}
df = pandas.DataFrame(dict, index=False)
```
Yes, I am a cricket geek.