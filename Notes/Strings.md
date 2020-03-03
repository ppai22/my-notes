## 1 - String Formatting

### 1 - Using %:

```python
>>> name = 'Pradeep'
>>> "My name is %s" % name
My name is Pradeep
```

```python
>>> name = 'Marcus Rashford'
>>> club = 'Manchester United'
>>> "%s is a great footballer. He plays for %s." % (name, club)
Marcus Rashford is a great footballer. He plays for Manchester United.
```

### 2 - Using str.format():

```python
>>> name = 'Pradeep'
>>> "My name is {}" .format(name)
My name is Pradeep
```

```python
>>> name = 'Marcus Rashford'
>>> club = 'Manchester United'
>>> "{} is a great footballer. He plays for {}.".format(name, club)
Marcus Rashford is a great footballer. He plays for Manchester United.
```

### f-strings:

```python
>>> name = 'Marcus Rashford'
>>> club = 'Manchester United'
>>> f"{name} is a great footballer. He plays for {club}."
Marcus Rashford is a great footballer. He plays for Manchester United.
```

(Reference)["https://realpython.com/python-f-strings/"]
