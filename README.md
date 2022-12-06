# ❄️ Advent of Code 2022 ❄️

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
    

## Day 4


```python
day04_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
```


```python
print(len(list(filter(lambda x: ((x[0]>=x[2] and x[1]<=x[3]) or (x[2]>=x[0] and x[3]<=x[1])), [[int(y) for y in pair.replace(',','-').split("-")] for pair in day04_input.split("\n")]))))
```

    2
    


```python
print(len(list(filter(lambda x: ((x[0]>=x[2] and x[0]<=x[3]) or (x[1]>=x[2] and x[1]<=x[3]) or (x[2]>=x[0] and x[2]<=x[1]) or (x[3]>=x[0] and x[3]<=x[1])), [[int(y) for y in pair.replace(',','-').split("-")] for pair in day04_input.split("\n")]))))
```

    4
    

## Day 5


```python
day05_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
```


```python
from functools import reduce

# First line of "one-liner solution" to get last elements of each stack
reduce(lambda c, d: c+d[-1], 
       # Second line performs rearrangements of stacks ("crane operations"), reduce function takes as arguments: 1) function (this line)
       reduce(lambda a,b: [a[i][:-b[0]] if i==b[1]-1 else a[i]+a[b[1]-1][:-b[0]-1:-1] if i==b[2]-1 else a[i] for i, s in enumerate(a)], 
              # Next line prepares array of crane actions, each line with 3 numbers
              [[int(line.split()[0]), int(line.split()[1]), int(line.split()[2])] for line in day05_input.split('\n\n')[1].replace('move ','').replace(' from ',' ').replace(' to ',' ').split('\n')], 
              # Next line prepares initial array of stacks in a format [['Z', 'N'], ['M', 'C', 'D'], ['P']]
              [list(filter(lambda x: x!=' ', [line[i*4+1] for line in day05_input.split('\n\n')[0].split('\n')[:-1]][::-1])) for i in range(len(day05_input.split('\n')[0][1::4]))]),
       '')
```

    CMZ


```python
reduce(lambda c, d: c+d[-1], 
       reduce(lambda a,b: [a[i][:-b[0]] if i==b[1]-1 else a[i]+a[b[1]-1][-b[0]:] if i==b[2]-1 else a[i] for i, s in enumerate(a)], 
              [[int(line.split()[0]), int(line.split()[1]), int(line.split()[2])] for line in day05_input.split('\n\n')[1].replace('move ','').replace(' from ',' ').replace(' to ',' ').split('\n')], 
              [list(filter(lambda x: x!=' ', [line[i*4+1] for line in day05_input.split('\n\n')[0].split('\n')[:-1]][::-1])) for i in range(len(day05_input.split('\n')[0][1::4]))]),
       '')
```

    MCD


## Day 6


```python
day06_input = """nppdvjthqldpwncqszvftbrmjlhg"""
```


```python
[1 if ((c!=day06_input[i+1]) and 
       (c!=day06_input[i+2]) and 
       (c!=day06_input[i+3]) and 
       (day06_input[i+1]!=day06_input[i+2]) and 
       (day06_input[i+1]!=day06_input[i+3]) and
       (day06_input[i+2]!=day06_input[i+3])) else 0 for i, c in enumerate(day06_input[:-3])].index(1)+4
```

    6


```python
[sum([1 if c2 in day06_input[i+i2+1:i+14] else 0 for i2, c2 in enumerate(day06_input[i:i+14])]) for i, c in enumerate(day06_input[:-13])].index(0)+14
```

    23


## Day 7