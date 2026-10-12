# 8) Sum of numbers 1 to 100.
n = 100
formula = n * (n + 1) // 2

total = 0
for i in range(1, n + 1):
    total += i

print('Формула:', formula)
print('Цикл:   ', total)
