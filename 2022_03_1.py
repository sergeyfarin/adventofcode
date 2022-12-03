input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
print(sum([sum([ord(i)-96 if ord(i)>96 else ord(i)-64+26 for i in set(r[:(len(r)//2)]).intersection(r[(len(r)//2):])]) for r in input.split("\n")]))
