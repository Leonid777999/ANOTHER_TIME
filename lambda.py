#############################################
lambda_list = [1, 2, 3, 4, 5, 6]


first_task = list(map(lambda n: n*3,lambda_list))
print(first_task)

###############################################

second_task = list(map(lambda n: n % 2 != 0, lambda_list))
print(second_task)


###############################################
import datetime
date_time = datetime.datetime.now()
print(date_time)

year = lambda x: x.year
month = lambda y: y.month
day = lambda z: z.day
hour = lambda a: a.hour
minute = lambda b: b.minute
second = lambda c: c.second

print(year(date_time), month(date_time), day(date_time), hour(date_time), minute(date_time),second(date_time))

###################################################
lambda_list_fourth = [1, 2, 3, 4, 5, 6]

fourth_task = list(filter(lambda n: n % 2 != 0, lambda_list))
print(fourth_task)




