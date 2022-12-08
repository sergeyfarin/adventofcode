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


```python
day07_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
```


```python
from functools import reduce
sum([
    reduce(lambda a, b: [a[0], 0] if a[1]==0 else [a[0], a[1]-1] if "$ cd .." in b else [a[0], a[1]+1] if "$ cd " in b else ([0, 0] if a[0]+int(b.split()[0])>100000 else [a[0]+int(b.split()[0]), a[1]]) if not (b[0] in "d$") else [a[0], a[1]], day07_input.split("\n")[i+1:], [0, 1])[0]
    if not "$ cd .." in c and "$ cd " in c else 0 for i, c in enumerate(day07_input.split("\n")[:-1])])
```

    95437


```python
reduce(lambda e, f: e if f==0 else e if f[1]<(30000000 - (70000000 - sum([int(d.split()[0]) if not d[0] in "d$" else 0 for d in day07_input.split("\n")[1:]]))) else e if f[1]>e[1] else f,
       [[c[5:], reduce(lambda a, b: [a[0], 0] if a[1]==0 else [a[0], a[1]-1] if "$ cd .." in b else [a[0], a[1]+1] if "$ cd " in b else [a[0]+int(b.split()[0]), a[1]] if not (b[0] in "d$") else [a[0], a[1]], day07_input.split("\n")[i+1:], [0, 1])[0]]
        if not "$ cd .." in c and "$ cd " in c else 0 for i, c in enumerate(day07_input.split("\n")[:-1])])[1]
```

    24933642


## Day 8


```python
day08_input = """30373
25512
65332
33549
35390"""
```


```python
from functools import reduce
reduce(lambda a, b: [a[0], a[1]+(1 if b[0]==0 or b[1]==0 or b[0]==len(a[0])-1 or b[1]==len(a[0][0])-1 else 
                                 1 if a[0][b[0]][b[1]]>max(a[0][b[0]][:b[1]]) or a[0][b[0]][b[1]]>max(a[0][b[0]][b[1]+1:]) or 
                                 a[0][b[0]][b[1]]>max([c[b[1]] for c in a[0][:b[0]]]) or 
                                 a[0][b[0]][b[1]]>max([c[b[1]] for c in a[0][b[0]+1:]]) else 0)],
       [(i,j) for i,a in enumerate(day08_input.split("\n"))  for j,b in enumerate(a)],
       [[[int(b) for j,b in enumerate(a)] for i,a in enumerate(day08_input.split("\n"))], 0])[1]
```

    21


```python
from functools import reduce
reduce(lambda a, b: [a[0], max(a[1], 0 if b[0]==0 or b[1]==0 or b[0]==len(a[0])-1 or b[1]==len(a[0][0])-1 else 
                                     reduce(lambda c, d: c if c[1]==1 else [c[0]+1, 0] if a[0][b[0]][b[1]]>d else [c[0]+1, 1], a[0][b[0]][b[1]-1::-1] ,[0,0])[0]*
                                     reduce(lambda c, d: c if c[1]==1 else [c[0]+1, 0] if a[0][b[0]][b[1]]>d else [c[0]+1, 1], a[0][b[0]][b[1]+1:] ,[0,0])[0]*
                                     reduce(lambda c, d: c if c[1]==1 else [c[0]+1, 0] if a[0][b[0]][b[1]]>d else [c[0]+1, 1], [d[b[1]] for d in a[0][b[0]-1::-1]] ,[0,0])[0]*
                                     reduce(lambda c, d: c if c[1]==1 else [c[0]+1, 0] if a[0][b[0]][b[1]]>d else [c[0]+1, 1], [d[b[1]] for d in a[0][b[0]+1:]] ,[0,0])[0])],
       [(i,j) for i,a in enumerate(day08_input.split("\n"))  for j,b in enumerate(a)],
       [[[int(b) for j,b in enumerate(a)] for i,a in enumerate(day08_input.split("\n"))], 0])[1]
```

    8


## Day 9