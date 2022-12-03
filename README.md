# ❄️ Advent of Code ❄️

Solving 2022 Advent of Code 🎄 (https://adventofcode.com/)
Days 1, 2 and 3 solved with python one-liners

## Day 1


```python
day01_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
```


```python
print(max([sum([int(y) if y!="" else 0 for y in x.split("\n")]) for x in day01_input.split("\n\n")]))
```

    24000
    


```python
print(sum(sorted([sum([int(y) if y!="" else 0 for y in x.split("\n")]) for x in day01_input.split("\n\n")])[-3:]))
```

    45000
    

## Day 2


```python
day02_input = """A Y
B X
C Z"""
```


```python
print(sum([(ord(x[2])-87+(6 if ord(x[2])-ord(x[0])==24 or ord(x[2])-ord(x[0])==21 else 3 if ord(x[2])-ord(x[0])==23 else 0)) for x in day02_input.split("\n")]))
```

    15
    


```python
print(sum([((ord(x[2])-88)*3+(ord(x[0])-65+ord(x[2])-89)%3+1) for x in day02_input.split("\n")]))
```

    12
    

## Day 3


```python
day03_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
```


```python
print(sum([sum([ord(i)-96 if ord(i)>96 else ord(i)-64+26 for i in set(r[:(len(r)//2)]).intersection(r[(len(r)//2):])]) for r in day03_input.split("\n")]))
```

    157
    


```python
print(sum([sum(map(lambda i: ord(i)-96 if ord(i)>96 else ord(i)-64+26, set(g[0]).intersection(g[1]).intersection(g[2]))) for g in [day03_input.split("\n")[i:i+3] for i in range(0, len(day03_input.split("\n")), 3)]]))
```

    70
    


```python

```
