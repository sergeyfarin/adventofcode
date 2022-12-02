input = """A Y
B X
C Z"""
print(sum([(ord(x[2])-87+(6 if ord(x[2])-ord(x[0])==24 or ord(x[2])-ord(x[0])==21 else 3 if ord(x[2])-ord(x[0])==23 else 0)) for x in input.split("\n")]))
