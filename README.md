# ❄️ Advent of Code 2022 ❄️

Solving 2022 Advent of Code 🎄 <https://adventofcode.com/>

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

```python
day09_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
```

```python
from functools import reduce
len(reduce(lambda a, b: 
  reduce(lambda c, d: [[c[0][0]+(1 if d=='R' else -1 if d=='L' else 0), c[0][1]+(1 if d=='U' else -1 if d=='D' else 0)], 
                       c[1] if d!='T' or (abs(c[0][0]-c[1][0])<=1 and abs(c[0][1]-c[1][1])==1) or (abs(c[0][0]-c[1][0])==1 and abs(c[0][1]-c[1][1])<=1) else 
                       [c[1][0]+(1 if c[0][0]>c[1][0] else -1), c[1][1]+(1 if c[0][1]>c[1][1] else -1)] if (abs(c[0][0]-c[1][0])>0 and abs(c[0][1]-c[1][1])>0) else 
                       [c[1][0]+(1 if c[0][0]>c[1][0] else -1 if c[0][0]<c[1][0] else 0), c[1][1]+(1 if c[0][1]>c[1][1] else -1 if c[0][1]<c[1][1] else 0)],
                       c[2] if c[1] in c[2] else c[2]+[c[1]]], 
         (b.split()[0]+'T')*int(b.split()[1]), a), day09_input.split("\n")+['F 1'], [[0, 0], [0, 0], [[0, 0]]])[2])
```

    13

```python
day09_input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
```

```python
from functools import reduce
len(
  reduce(lambda a, b: 
    reduce(lambda c, d: 
      reduce(lambda e, f: [[[e[0][0][0]+(0 if f>0 else 1 if d=='R' else -1 if d=='L' else 0), e[0][0][1]+(0 if f>0 else 1 if d=='U' else -1 if d=='D' else 0)]]+
                           [e[0][i] if i!=f or (abs(e[0][i-1][0]-e[0][i][0])<=1 and abs(e[0][i-1][1]-e[0][i][1])==1) or (abs(e[0][i-1][0]-e[0][i][0])==1 and abs(e[0][i-1][1]-e[0][i][1])<=1) else 
                            [e[0][i][0]+(1 if e[0][i-1][0]>e[0][i][0] else -1), e[0][i][1]+(1 if e[0][i-1][1]>e[0][i][1] else -1)] if (abs(e[0][i-1][0]-e[0][i][0])>0 and abs(e[0][i-1][1]-e[0][i][1])>0) else 
                            [e[0][i][0]+(1 if e[0][i-1][0]>e[0][i][0] else -1 if e[0][i-1][0]<e[0][i][0] else 0), e[0][i][1]+(1 if e[0][i-1][1]>e[0][i][1] else -1 if e[0][i-1][1]<e[0][i][1] else 0)]
                            for i in range(1, 10)],
                           e[1] if e[0][9] in e[1] else e[1]+[e[0][9]]], range(10), c), 
      (b.split()[0])*int(b.split()[1]), a), day09_input.split("\n")+['F 1'], [[[0, 0]]*10, [[0, 0]]])[1])
```

    36

## Day 10

```python
day10_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
```

```python
from functools import reduce
reduce(lambda a, b: [
  a[0]+(1 if b[:4]=="noop" else 2 if b[:4]=="addx" else 0),
  a[1]+(0 if b[:4]=="noop" else int(b.split()[1]) if b[:4]=="addx" else 0),
  a[2]+((a[0]+1)*a[1] if (a[0]+21)%40==0 else (a[0]+2)*a[1] if ((a[0]+22)%40==0 and b[:4]=="addx") else 0)
  ] ,day10_input.split("\n"), [0, 1, 0])[2]
```

    13140

```python
from functools import reduce
print(reduce(lambda a, b: [
  a[0]+(1 if b[:4]=="noop" else 2 if b[:4]=="addx" else 0),
  a[1]+(0 if b[:4]=="noop" else int(b.split()[1]) if b[:4]=="addx" else 0),
  a[2]+("#" if abs((a[0])%40-a[1])<=1 else ".")+("\n" if (a[0]+1)%40==0 else "")+
  (("#" if abs((a[0]+1)%40-a[1])<=1 else ".")+("\n" if (a[0]+2)%40==0 else "") if b[:4]=="addx" else "")
  ] ,day10_input.split("\n"), [0, 1, ""])[2])
```

    ##..##..##..##..##..##..##..##..##..##..
    ###...###...###...###...###...###...###.
    ####....####....####....####....####....
    #####.....#####.....#####.....#####.....
    ######......######......######......####
    #######.......#######.......#######.....

```python
real_day10_input = """addx 2
addx 15
addx -11
addx 6
noop
noop
noop
addx -1
addx 5
addx -1
addx 5
noop
noop
noop
noop
noop
addx 7
addx -1
addx 3
addx 1
addx 5
addx 1
noop
addx -38
noop
addx 1
addx 6
addx 3
noop
addx -8
noop
addx 13
addx 2
addx 3
addx -2
addx 2
noop
addx 3
addx 9
addx -2
addx 2
addx -10
addx 11
addx 2
addx -14
addx -21
addx 2
noop
addx 5
addx 29
addx -2
noop
addx -19
noop
addx 2
addx 11
addx -10
addx 2
addx 5
addx -9
noop
addx 14
addx 2
addx 3
addx -2
addx 3
addx 1
noop
addx -37
noop
addx 13
addx -8
noop
noop
noop
noop
addx 13
addx -5
addx 3
addx 3
addx 3
noop
noop
noop
noop
noop
noop
noop
addx 6
addx 3
addx 1
addx 5
addx -15
addx 5
addx -27
addx 30
addx -23
addx 33
addx -32
addx 2
addx 5
addx 2
addx -16
addx 17
addx 2
addx -10
addx 17
addx 10
addx -9
addx 2
addx 2
addx 5
addx -29
addx -8
noop
noop
noop
addx 19
addx -11
addx -1
addx 6
noop
noop
addx -1
addx 3
noop
addx 3
addx 2
addx -3
addx 11
addx -1
addx 5
addx -2
addx 5
addx 2
noop
noop
addx 1
noop
noop"""
```

```python
from functools import reduce
print(reduce(lambda a, b: [
  a[0]+(1 if b[:4]=="noop" else 2 if b[:4]=="addx" else 0),
  a[1]+(0 if b[:4]=="noop" else int(b.split()[1]) if b[:4]=="addx" else 0),
  a[2]+("#" if abs((a[0])%40-a[1])<=1 else ".")+("\n" if (a[0]+1)%40==0 else "")+
  (("#" if abs((a[0]+1)%40-a[1])<=1 else ".")+("\n" if (a[0]+2)%40==0 else "") if b[:4]=="addx" else "")
  ] ,real_day10_input.split("\n"), [0, 1, ""])[2])
```

    ####..##....##..##..###....##.###..####.
    #....#..#....#.#..#.#..#....#.#..#.#....
    ###..#.......#.#..#.#..#....#.#..#.###..
    #....#.......#.####.###.....#.###..#....
    #....#..#.#..#.#..#.#....#..#.#.#..#....
    #.....##...##..#..#.#.....##..#..#.####.

## Day 11

```python
day11_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
```

```python
from functools import reduce
(lambda z: (z[0])*(z[1]))(sorted([j[6] for j in 
  reduce(lambda a, b: 
    reduce(lambda c, d: 
      # c,
      reduce(lambda e, f: 
        [
          [i[0],
          ([i[1][0]] if i[0]!=d[0] and len(i[1])>0 else [])+
          (i[1][1:] if len(i[1])>1 else [])+
          ([] if len(e[d[0]][1])==0 else (
            [(lambda x, y: x+y if d[2][1]=='+' else x*y if d[2][1]=='*' else 999)(
              e[d[0]][1][0] if d[2][0]=='old' else int(d[2][0]), 
              e[d[0]][1][0] if d[2][2]=='old' else int(d[2][2]))//3] if i[0]==(
            d[4] if (lambda x, y: x+y if d[2][1]=='+' else x*y if d[2][1]=='*' else 999)(
              e[d[0]][1][0] if d[2][0]=='old' else int(d[2][0]), 
              e[d[0]][1][0] if d[2][2]=='old' else int(d[2][2]))//3%d[3]==0
            else d[5]) else [])),
          i[2],
          i[3],
          i[4],
          i[5],
          i[6]+(1 if i[0]==d[0] and len(i[1])>0 else 0)
          ] for i in e
        ]
        , c[d[0]][1], c),
      a, a),
    range(20),
    [[int(m.replace(":"," ").split()[1]),
    [int(i) for i in m.split("\n")[1].replace(",","").split()[2:]], 
    m.split("\n")[2].split()[3:],
    int(m.split("\n")[3].split()[3]), 
    int(m.split("\n")[4].split()[5]),
    int(m.split("\n")[5].split()[5]),
    0] for m in day11_input.split("\n\n")])])[-2:])
```

    10605

```python
from functools import reduce
(lambda z: (z[0])*(z[1]))(sorted([j[6] for j in 
  reduce(lambda a, b: 
    reduce(lambda c, d: 
      # c,
      reduce(lambda e, f: 
        [
          [i[0],
          ([i[1][0]] if i[0]!=d[0] and len(i[1])>0 else [])+
          (i[1][1:] if len(i[1])>1 else [])+
          ([] if len(e[d[0]][1])==0 else (
            [(lambda x, y: x+y if d[2][1]=='+' else x*y%(reduce(lambda g, h: g*h, [j[3] for j in c])) if d[2][1]=='*' else 999)(
              e[d[0]][1][0] if d[2][0]=='old' else int(d[2][0]), 
              e[d[0]][1][0] if d[2][2]=='old' else int(d[2][2]))] if i[0]==(
            d[4] if (lambda x, y: x+y if d[2][1]=='+' else x*y if d[2][1]=='*' else 999)(
              e[d[0]][1][0] if d[2][0]=='old' else int(d[2][0]), 
              e[d[0]][1][0] if d[2][2]=='old' else int(d[2][2]))%d[3]==0
            else d[5]) else [])),
          i[2],
          i[3],
          i[4],
          i[5],
          i[6]+(1 if i[0]==d[0] and len(i[1])>0 else 0)
          ] for i in e
        ]
        , c[d[0]][1], c),
      a, a),
    range(10000),
    [[int(m.replace(":"," ").split()[1]),
    [int(i) for i in m.split("\n")[1].replace(",","").split()[2:]], 
    m.split("\n")[2].split()[3:],
    int(m.split("\n")[3].split()[3]), 
    int(m.split("\n")[4].split()[5]),
    int(m.split("\n")[5].split()[5]),
    0] for m in day11_input.split("\n\n")])])[-2:])
```

    2713310158

## Day 12

Not a one-liner solution

```python
day12_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
```

```python
Arr = [[c for c in l] for l in day12_input.replace('S','a').split('\n')]
S = day12_input.find('S')//(len(day12_input.split('\n')[0])+1), day12_input.find('S')%(len(day12_input.split('\n')[0])+1)
E = day12_input.find('E')//(len(day12_input.split('\n')[0])+1), day12_input.find('E')%(len(day12_input.split('\n')[0])+1)
stack=[S, [-1,-1]]
for i,j in stack:
  if i!=-1:
    for k, l in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
      if k>=0 and l>=0 and k<len(Arr) and l<len(Arr[0]):
        if Arr[k][l]=='E' and ord(Arr[i][j])>=ord('y'):
          print(stack[:stack.index([i, j])].count([-1,-1])+1)
          break
        elif ord(Arr[k][l])<=(ord(Arr[i][j])+1) and not [k,l] in stack:
          stack+=[[k,l]]
    else:
      continue
    break
  else: 
    stack+=[[-1, -1]]
```

    31

```python
Arr = [[c for c in l] for l in day12_input.replace('E','z').replace('S','a').split('\n')]
S = day12_input.find('S')//(len(day12_input.split('\n')[0])+1), day12_input.find('S')%(len(day12_input.split('\n')[0])+1)
E = day12_input.find('E')//(len(day12_input.split('\n')[0])+1), day12_input.find('E')%(len(day12_input.split('\n')[0])+1)
stack=[E, [-1, -1]]
for i, j in stack:
  if i!=-1:
    for k, l in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
      if k>=0 and l>=0 and k<len(Arr) and l<len(Arr[0]):
        if Arr[k][l]=='a' and ord(Arr[i][j])<=ord('b'):
          print(stack[:stack.index([i, j])].count([-1,-1])+1)
          break
        elif ord(Arr[k][l])>=(ord(Arr[i][j])-1) and not [k,l] in stack:
          stack+=[[k,l]]
    else:
      continue
    break
  else:
    stack+=[[-1, -1]]  
```

    29

## Day 13

Not a one-liner solution

```python
day13_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
```

```python
count = 0
for i, l in enumerate([[[int(k) if not k in '[]' else k for k in j.split()] for j in i.split('\n')] for i in day13_input.replace('[','[ ').replace(']',' ] ').replace(',',' ').split("\n\n")]):
        s1 = l[0]
        s2 = l[1]
        for j in range(max(len(s1), len(s2))*3):
                if s1[j]==s2[j]: continue
                if s2[j]==']':
                        break
                if s1[j]==']':
                        count+=i+1
                        break
                if s2[j]=='[':
                        s1=s1[:j]+['[']+[s1[j]]+[']']+s1[j+1:]
                        continue
                if s1[j]=='[':
                        s2=s2[:j]+['[']+[s2[j]]+[']']+s2[j+1:]
                        continue
                if s1[j]>s2[j]:
                        break
                if s1[j]<s2[j]:
                        count+=i+1
                        break
                raise Exception("Unknown case", s1[j], s2[j])
print(count)
```

    13

```python
count = 0
list = [[int(k) if not k in '[]' else k for k in i.split()] for i in (day13_input+'\n[[2]]\n[[6]]').replace('[','[ ').replace(']',' ] ').replace(',',' ').replace('\n\n','\n').split("\n")]
for i in range(len(list)-1):
  s1 = list[i]
  for k in range(i+1,len(list)):
    s2 = list[k]
    for j in range(max(len(s1), len(s2))*3):
      if s1[j]==s2[j]: continue
      if s2[j]==']':
              list[i], list[k] = list[k], list[i]
              s1 = list[i]
              s2 = list[k]
              break
      if s1[j]==']':
              break
      if s2[j]=='[':
              s1=s1[:j]+['[']+[s1[j]]+[']']+s1[j+1:]
              continue
      if s1[j]=='[':
              s2=s2[:j]+['[']+[s2[j]]+[']']+s2[j+1:]
              continue
      if s1[j]>s2[j]:
              list[i], list[k] = list[k], list[i]
              s1 = list[i]
              s2 = list[k]
              break
      if s1[j]<s2[j]:
              break
      raise Exception("Unknown case", s1[j], s2[j])
print((list.index(['[', '[', 2, ']', ']'])+1)*(list.index(['[', '[', 6, ']', ']'])+1))
```

    140

## Day 14

```python
day14_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
```

```python
xmin, xmax, ymin, ymax = [
  min([int(n) for n in day14_input.replace(',',' ').replace('-','').replace('>','').split()[::2]])-1,
  max([int(n) for n in day14_input.replace(',',' ').replace('-','').replace('>','').split()[::2]])+2,
  0,
  max([int(n) for n in day14_input.replace(',',' ').replace('-','').replace('>','').split()[1::2]])+2]
Arr = [''.join(['.' for x in range(xmax-xmin)]) for y in range(ymax-ymin)]
for l in day14_input.split('\n'):
  coords = [[int(c.split(',')[0])-xmin, int(c.split(',')[1])-ymin] for c in l.replace('-','').replace('>','').split()]
  x0, y0 = coords[0]
  for x1, y1 in coords[1:]:
    for x in range(min(x0,x1), max(x0,x1)+1):
      for y in range(min(y0,y1), max(y0,y1)+1):
        Arr[y]=Arr[y][:x]+'#'+Arr[y][x+1:]
    x0, y0 = x1, y1
  
c=0
while True:
  if Arr[0][500-xmin]!='.': 
    raise Exception('500, 0  is occupied!', Arr)
  x=500-xmin
  for y in range(1, ymax):
    if Arr[y][x]=='.': 
      continue
    if x>0:
      if Arr[y][x-1]=='.':
        x-=1
        continue
    if x<(xmax-xmin-2):
      if Arr[y][x+1]=='.':
        x+=1
        continue
  
    Arr[y-1]=(Arr[y-1][:x] if x>0 else '')+'o'+(Arr[y-1][x+1:] if x<(xmax-xmin-1) else '')
    c+=1
    break
  else:
    break
  
print(str(c)+'\n\n'+'\n'.join(Arr))
```

    24

    ............
    ............
    .......o....
    ......ooo...
    .....#ooo##.
    ....o#ooo#..
    ...###ooo#..
    .....oooo#..
    ..o.ooooo#..
    .#########..
    ............

```python
xmin, xmax, ymin, ymax = [
  min([int(n) for n in day14_input.replace(',',' ').replace('-','').replace('>','').split()[::2]])-1,
  max([int(n) for n in day14_input.replace(',',' ').replace('-','').replace('>','').split()[::2]])+2,
  0,
  max([int(n) for n in day14_input.replace(',',' ').replace('-','').replace('>','').split()[1::2]])+3]
xmin = min(xmin, 500-ymax-2)
xmax = max(xmax, 500+ymax+2)
Arr = [''.join(['.' for x in range(xmax-xmin)]) for y in range(ymax-ymin)]
for l in day14_input.split('\n')+[str(xmin)+','+str(ymax-1)+' '+str(xmax)+','+str(ymax-1)]:
  coords = [[int(c.split(',')[0])-xmin, int(c.split(',')[1])-ymin] for c in l.replace('-','').replace('>','').split()]
  x0, y0 = coords[0]
  for x1, y1 in coords[1:]:
    for x in range(min(x0,x1), max(x0,x1)+1):
      for y in range(min(y0,y1), max(y0,y1)+1):
        Arr[y]=Arr[y][:x]+'#'+Arr[y][x+1:]
    x0, y0 = x1, y1
  
c=0
while True:
  if Arr[0][500-xmin]!='.': 
    break
  x=500-xmin
  for y in range(1, ymax):
    if Arr[y][x]=='.': 
      continue
    if x>0:
      if Arr[y][x-1]=='.':
        x-=1
        continue
    if x<(xmax-xmin-2):
      if Arr[y][x+1]=='.':
        x+=1
        continue
  
    Arr[y-1]=(Arr[y-1][:x] if x>0 else '')+'o'+(Arr[y-1][x+1:] if x<(xmax-xmin-1) else '')
    c+=1
    break
  else:
    break
  
print(str(c)+'\n\n'+'\n'.join(Arr))
```

    93

    ..............o.............
    .............ooo............
    ............ooooo...........
    ...........ooooooo..........
    ..........oo#ooo##o.........
    .........ooo#ooo#ooo........
    ........oo###ooo#oooo.......
    .......oooo.oooo#ooooo......
    ......oooooooooo#oooooo.....
    .....ooo#########ooooooo....
    ....ooooo.......ooooooooo...
    #############################

## Day 15