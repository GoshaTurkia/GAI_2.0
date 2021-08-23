# Task 1
a = input()
l = len(a)
a = int(a)
s = 0
for i in range(l):
    s += a % 10
    a = (a - (a % 10)) // 10
print(s)

# Task 2
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
for i in range(len(lst)):
    if lst[i] < 30 and lst[i] % 2 == 0: print(lst[i], end=' ')
for i in range(len(lst)):
    if lst[i] % 3 == 0: print(lst[i])

# Task 3
a = input()
if len(a) % 2 == 0:
    if a[:len(a) // 2] == a[len(a) // 2:][::-1]: print('Палиндром')
    else: print('Не палиндром')
else:
    if a[:len(a) // 2] == a[len(a) // 2 + 1:][::-1]: print('Палиндром')
    else: print('Не палиндром')

# Task 4
a = [1, 'g', 'f', 23, 'v']
b = [1, 2, 3, 4, 5]
d = {a[i]:b[i] for i in range(len(a))}
print(d)

# Task 5
def f(s):
    s = s[::-1]
    for i in s:
        print(i)
f('asdgfhjasdg')

# Task *
def month_to_season(n):
    d = {'winter':[1,2,12], 'spring':[3,4,5], 'summer':[6,7,8], 'authumn':[9,10,11]}
    for i in d.keys():
        if n in d[i]:
            return i
print(month_to_season(5))

# 21.08
# Task 1
a = 'pythonist'
d = {x:a.count(x) for x in list(set(list(a)))}
print(d)

# Task 2
with open('t.txt') as f:
    d = {}
    a = f.readlines()
    for i in range(len(a)):
        if a[i] == '\n':
            continue
        else:
            a[i] = a[i].strip()
            b = a[i].split(':')
            try:
                b[1] = int(b[1])
            except ValueError:
                pass
            d[b[0]] = b[1]
print(d)