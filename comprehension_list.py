###################################################
first_task_list = [1, -2, 3, -4, 5, 6, -7, 8, -9]

new_first_task_list = [x for x in first_task_list if x < 0]

print(new_first_task_list)

####################################################
second_task_list = ['one', 'second', 'third', 'fourth', 'fifth', 'sixth']

new_second_task_list = [x for x in second_task_list if len(x) == 5]

print(new_second_task_list)

#####################################################
third_task_list = [11, 13, 25, 26, 38, 39]

new_third_task_list = [x for x in third_task_list if x % 13 == 0]

print(new_third_task_list)

########################################################
fourth_task_list = ['fred', 'John', 'peter', 'Jimmy', 'arnold']

new_fourth_task_list = [x for x in fourth_task_list if x != x.lower()]

print(new_fourth_task_list)

#########################################################
fifth_task_list = [1, 7, 11, 14, 23, 24]

new_fifth_task_list = [x for x in fifth_task_list if not any(map(lambda y: int(y) == 0 or x%int(y) != 0, str(x)))]
print(new_fifth_task_list)
