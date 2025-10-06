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
# rows = 5
# for i in range(1, rows+1):
#     num = 1

#     for j in range(rows, 0, -1):
#         if j > i:
#             print(' ', end=' ')
#         else:
#             print(num, end=' ')
#             num += 1
#     print()

    
# print()



'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
'''
curr_list = prev_list = []
rows = 7

for i in range(1, rows+1):
    for j in range(1, i + 1):
        if len(prev_list) in [0, 1] or j in [i, 1]:
            num = 1

        else:
            num = prev_list[j - 1] + prev_list[j - 2]

        print(num, end=' ')
        curr_list.append(num)
    
    print()

    prev_list = curr_list.copy()
    curr_list = []


print()



'''
1 2 3 4 5
2 2 3 4 5
3 3 3 4 5
4 4 4 4 5
5 5 5 5 5
'''
size = 5

for i in range(1, size + 1):
    for j in range(1, size + 1):
        if i >= j:
            print(i, end=' ')
        
        else:
            print(j, end=' ')

    print()


print()



'''
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64 
'''
rows = 8

for i in range(1, rows + 1):
    for j in range(i, (i + 1) * i, i): # really really bad compared to the solution T_T
        print(j, end='  ')

    print()
    
    
print()



'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''
rows = 5

for i in range(1, rows + 1):
    print('  ' * (rows - i) + '* '*i)

print()



'''
* * * * *  
* * * *  
* * *  
* *  
*
'''
rows = 5

for i in range(rows):
    print('* ' * (rows - i))


print()



'''
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
'''
rows = 6

for i in range(rows):
    print(' ' * i + '* ' * (rows - i))


print()



'''
*****
 ****
  ***
   **
    *
'''
rows = 5

for i in range(rows):
    print(' ' * i + '*' * (rows - i))


print()



'''
      *   
     *  *   
    *  *  *   
   *  *  *  *   
  *  *  *  *  *   
 *  *  *  *  *  *   
*  *  *  *  *  *  *   
'''
rows = 7

for i in range(rows):
    print(' ' * (rows - 1 - i) + '*  ' * (i + 1))


print()



'''
*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
 
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
*  
'''
rows = 5

for i in range(rows):
    print('* ' * (i + 1))

print()

for i in range(rows):
    print('* ' * (rows - i))


print()



'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''
rows = 5

for i in range(rows):
    print('* ' * (i + 1))


for i in range(1, rows):
    print('* ' * (rows - i))


print()



'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''
rows = 5

for i in range(rows + 1):
    print('  ' * (rows - i) + '* ' * (i + 1))

for i in range(rows, 0, -1):
    print('  ' * (rows - i + 1) + '* ' * (i))


print()



'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
rows = 5

for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '* ' * i)

for j in range(1, rows + 1):
    print(' ' * (rows - j) + '* ' * j)


print()



'''
****************
*******__*******
******____******
*****______*****
****________****
***__________***
**____________**
*______________*
'''
rows = 8

for i in range(rows):
    print('*' * ((rows - i)) + '__' * i + '*' * ((rows - i)))


print()



'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
'''
rows = 6

for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * i)

for j in range(rows - 1, 0, -1):
    print(' ' * (rows - j) + '* ' * j)


print()



'''
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''
rows = 5

for i in range(1, rows + 1):
    if i == 1:
        print(' ' * (rows - i) + '*')
    
    else:
        print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + '*')

for j in range(rows - 1, 0, - 1):
    if j == 1:
        print(' ' * (rows - j) + '*')
    
    else:
        print(' ' * (rows - j) + '*' + ' ' * (2 * j - 3) + '*')