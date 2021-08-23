# Task 1
print(3 / 2, 3 // 2, 2000**200, sep='\n')

# Task 2
a = input()
a = a.lower()
if a[0] == 'a' or len(a) == 10 or 97 <= ord(a[-1]) <= 122:
    print('Yes')
else: print('No')

# Task 3
a, b, c = int(input()), int(input()), int(input())
l = [a, b, c]
l.sort(reverse=True)
print(l[0], l[2], l[1], sep='\n')

# Task 4
ticket = [int(i) for i in input().split()]
if sum(ticket[:3]) == sum(ticket[3:]): print('Счастливый')
else: print('Обычный')

# Task 5
s = input()
for ind, el in enumerate(s):
    if ind % 3 == 0: print(el, ind)

# Task 6
l = [1, 2, 'hello', 4]
l[2] = 3

# Task 7
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
b = [1, 3, 5]
print(len(b), max(b), sep='\n')

# Task 8
a = 'asKHBKckjKbkcbTjhTjR'
b = ''
for i in range(len(a)):
    if a[i] == 'o': b += 'a'
    elif a[i] == 'T': b += 'R':
    else: b += a[i]

# Task 9
print(len('1, 2, 3, 4, 5, 6, 7, 8, 9, 0'.split(', ')))

# Task 10
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
a = ['3', '5', '7', '9']
print(', '.join(a))

# Task 11
a = 'HeLlo, wOrld!'
print(a[-6:-1:1], a[2]+a[5]+a[8])

# Task 12
a = ['a', 'b', 'c', 'a', 'c', 'z']
s = {}
for i in range(len(a)):
    if a[i] not in s.keys(): s[a[i]] = a.count(a[i])
for i in s.keys():
    print(i, s[i])

# Task 13
import numpy as np
m = np.array([[1, 0, 2], [2, 4, 1], [-1, -3, 2]])
a = np.linalg.det(m)
b = np.linalg.det(np.linalg.inv(m))
print(a, b, a*b)

# Task 14
def mymax(a, b, c=5):
    if a >= b and a >= c: return a
    elif b >= a and b >= c: return b
    else: return c
A, B, C = int(input()), int(input()), int(input())
print(mymax(A, B, C))

# Task 15
with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        a = inp.readlines()
        a = [i.strip() for i in a]
        print(len(a))
        out.write(str(len(a))+'\n')
        s = 0
        for i in range(len(a)):
            if (i+1) % 2 == 0:
                print(a[i])
                out.write(a[i]+'\n')
            if '1' in a[i] or '2' in a[i] or '3' in a[i] or '4' in a[i] or '5' in a[i] or '6' in a[i] or '7' in a[i] or '8' in a[i] or '9' in a[i]:
                for j in range(len(a[i])):
                    try:
                        s += int(a[i][j])
                    except:
                        continue
        print(s)
        out.write(str(s)+'\n')

# Task 16
name = input('Введите Ваше имя')
birthday = input('Введите дату рождения в формате дд/мм/гггг')
dates = {name: birthday.split('/')}

# Task 18
try:
    print(int('+'))
except ValueError:
    print('Хватит косячить!')

# Task 19
class Point:
    from math import sqrt
    def __init__(self, coordinates='0.0 0.0'):
        self.coordinates = [float(i) for i in coordinates]
        self.x = self.coordinates[0]
        self.y = self.coordinates[1]
    def move(self, coord):
        coord = [float(i) for i in coord]
        self.x = coord[0]
        self.y = coord[1]
    def distance(self, point1, point2='0.0 0.0'):
        point1 = [float(i) for i in point1]
        point2 = [float(i) for i in point2]
        disct = sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
        return disctance
