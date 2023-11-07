null = 5
another_value = 0

try:
    null_division = null / another_value
    print(null_division)
except ZeroDivisionError as zero:
    print("An exception:", zero)
finally:
    print("But we will continue")


##################################################
class SalaryException(Exception):
    '''exception about unacceptable level of salary'''


try:
    proposed_salary = int(input())
    if proposed_salary < 1500:
        raise SalaryException("Unacceptable salary")
except SalaryException as s:
    print(s)
finally:
    print("I`ll think about it")

