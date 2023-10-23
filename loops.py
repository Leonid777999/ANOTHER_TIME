#########################################################
list = ['orange', 'apple', 'banana', 'cherry']

for i in list:
    print(i)

for i in list:
    if i == 'apple':
        print(i)

for i in list:
    print(i),
    print(len(i))

#########################################################
for i in range(2, 100):
    print(i)

for i in range (2,100):
    if i < 16:
        print(i)

n = 0
while n < 16:
    print(n)
    n = n+1


n = 3
while n <= 33:
    print(n)
    n = n+1


############################################################
list = ['orange', 'apple', 'banana', 'cherry']

for i in list:
    print(i)
    if i == 'banana':
        break

