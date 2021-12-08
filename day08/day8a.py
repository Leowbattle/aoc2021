import itertools as it

f = open("input")

patterns = it.chain.from_iterable(l.split('|')[1].split() for l in f.read().splitlines())
score = len(list(filter(lambda p: len(p) in [2, 4, 3, 7], patterns)))
print(score)