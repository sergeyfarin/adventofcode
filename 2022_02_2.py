input = """A Y
B X
C Z"""
print(sum([((ord(x[2])-88)*3+(ord(x[0])-65+ord(x[2])-89)%3+1) for x in input.split("\n")]))
