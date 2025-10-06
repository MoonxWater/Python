'''
*
* *
* * *
* * * *
'''
for i in range(1, 5):
    print('* '*i)


print()



'''
0
0 1
0 1 2
0 1 2 3
'''
prefix = ''

for i in range(4):
    prefix = prefix + str(i) + ' '
    print(prefix)


print()



'''
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''
for i in range(6, 0, -1):
    print('* '*i)


print()



'''
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
0
'''
for i in range(6):
    for j in range(6 - i):
        print(j, end=' ')
    
    print()


print()



'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
prefix = ''

for i in range(1, 6):
    prefix = prefix + str(i) + ' '
    print(prefix)


print()



'''
1 1 1 1 1
2 2 2 2 
3 3 3
4 4
5
'''
num = 1

for i in range(5, 0, -1):
    prefix = (str(num) + ' ') * i
    print(prefix)
    num += 1


print()



'''
5 5 5 5 5
5 5 5 5
5 5 5 
5 5
5
'''
for i in range(5, 0, -1):
    print('5 '*i)


print()



'''
1
3 3
5 5 5
7 7 7 7
9 9 9 9 9
'''
num = 1

for i in range(1, 6):
    print((str(num) + ' ') * i)

    num += 2


print()



'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2 
1
'''
rows = 5
for i in range(rows, 0, -1):
    print((str(rows) + ' ') * i)
    rows -= 1


print()



'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
suffix = ''

for i in range(1, 6):
    suffix = str(i) + ' ' + suffix
    print(suffix)


print()



'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1 
1
'''
rows = 5

for i in range(rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    
    print()

    
print()



'''
1
3 2
6 5 4
10 9 8 7
'''
rows = 4
count = 0


for i in range(1, rows + 1):
    count += i

    for j in range(count, count - i, -1):
        print(j, end=' ')
    
    print()



print()



'''
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
'''
rows = 5

for i in range(1, rows + 1):
    print((10 - i * 2) * ' ', end='')
    
    for j in range(1, i + 1):
        print(j, end=' ')

    print()


print()


# solution
rows = 5
for i in range(1, rows+1):
    num = 1

    for j in range(rows, 0, -1):
        if j > i:
            print(' ', end=' ')
        else:
            print(num, end=' ')
            num += 1
    print()

    
print()



'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
'''