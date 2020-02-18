from itertools import combinations

filename = 'd_quite_big'
with open(f'./{filename}.in', 'r') as file:
    data = file.read()

data = data.split('\n')
M, N = [int(row) for row in data[0].split(' ')]
slices = [int(row) for row in data[1].split(' ')]

total = 0
n_slices_max = 0

while total + slices[n_slices_max] < M:
    total = total + slices[n_slices_max]
    n_slices_max += 1

pizza = list(range(n_slices_max))


def compute(pizza):
    output = 0
    for element in pizza:
        output = output + slices[element]
    return output


best = dict()
best['n'] = 0
best['pizza'] = []

# print("max", n_slices_max)
print()

try:
    for i in reversed(range(2, n_slices_max+1)):
            # print(i)
        for pizza in combinations(range(N), i):
            # print(pizza)
            n = compute(pizza)

            if n > best['n'] and n < M:
                best['n'] = n
                print(n)
                best['pizza'] = pizza
            elif n == M:
                best['n'] = n
                best['pizza'] = pizza
                break
            elif n > M:
                # print(n, 'break')
                break
except KeyboardInterrupt:
    pass


# print(list(best['pizza']))
result = f'{str(len(best["pizza"]))}\n{" ".join([str(row) for row in best["pizza"]] )}'

print(result)
with open(f'./{filename}.out', 'w') as file:
    file.write(result)
