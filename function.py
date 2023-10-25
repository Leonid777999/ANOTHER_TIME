##############################################
def hello_world():
    print("Hello world!")

hello_world()

##############################################
def my_name(name, surname):
    print('Hello my name is ' + name, '' + surname)


my_name('Algol', 'Petrol')


def my_name(name='Algol', surname='Petrol'):
    print('Hello my name is ' + name, '' + surname)

my_name()

##################################################
def print_person_info(name:str, surname:str, maritalStatus= 'unknown', *age):
    print(name, surname, maritalStatus, age)


print_person_info('John', 'Fooler', 'single', 35)
print_person_info('John', 'Fooler')

####################################################
def person_data(**kwargs):
    print(kwargs['name'],kwargs['surname'])


person_data(age=34, name='Joshua', sex='male', surname='Habber', height=1.45)

####################################################
def car_models(*cars):
    print('The first car models is', cars[0])

car_models('Toyota', 'Lamborghini', 'Ferrari', 'Hyundai', 'Honda')




