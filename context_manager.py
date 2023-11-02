###############################################
file = open("first_task_file.txt", "a")
file.write("This text contains numbers 21, 23 and very many letters and words - nearly 345")

###############################################
file = open("first_task_file.txt", "r")
dig = [int(x) for x in file.readline() if x.isdigit()]
print(sum(dig))

###############################################







