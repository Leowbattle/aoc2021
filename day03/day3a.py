from statistics import mode

f = open("input")
lines = f.read().splitlines()
width = len(lines[0])

gamma = int("".join(mode(l[n] for l in lines) for n in range(width)), base=2)
epsilon = ~gamma & ((1 << width) - 1)
print(f"γ = {gamma} ε = {epsilon}")
print(f"γε = {gamma * epsilon}")