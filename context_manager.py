###############################################
file = open("first_task_file.txt", "a")
file.write("This text contains numbers 21, 23 and very many letters and words - nearly 345")

###############################################
file = open("first_task_file.txt", "r")
dig = [int(x) for x in file.readline() if x.isdigit()]
print(sum(dig))


###############################################
with open("first_task_file.txt", "r") as len_file:
    dig_len = len_file.readline()
    print(max(dig_len.split(), key=len))

################################################
file.close()
print(file.closed)

################################################
a = '''aaaa aaaaaaa 
yyyyyyyyyyyy  yyyyyyyy yyyyyyyy   
xxxxxxxx   xxxxxxxxxxxxx
bbbbbbbbbbbbbbbbbbbb \n'''

b = '''000000000000 00000000
444444 444444 44444444
7777 77777 777777
999999 9999 9999999999'''

second_file = open("second_file.txt", 'w')
second_file.write(b)

with open("first_file.txt", 'a') as first_file:
    first_file.write(a)
    with open("second_file.txt", "r") as second_file:
        second_lines = second_file.readlines()
    first_file.writelines(second_lines[1:-1])

with open("first_file.txt", 'r') as first_file:
    print(first_file.read())

###############################################
with open("first_file.txt") as first_file, open("second_file.txt") as second_file:
            for first_file, second_file in zip(first_file, second_file):
                print(first_file, second_file)

#################################################











