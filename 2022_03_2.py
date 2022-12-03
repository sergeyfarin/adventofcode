input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
print(sum([sum(map(lambda i: ord(i)-96 if ord(i)>96 else ord(i)-64+26, set(g[0]).intersection(g[1]).intersection(g[2]))) for g in [input.split("\n")[i:i+3] for i in range(0, len(input.split("\n")), 3)]]))
