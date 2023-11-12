############################
class First:

    first_class = 1
    second_second = 2

    def __init__(self, first: str, second: int):
        self.first = first
        self.second = second

###########################
class A:
    def __init__(self, first_attr: str, second_attr: int):
        self.first = first_attr
        self.second = second_attr

    def __str__(self):
        return "{} {}".format(self.first, self.second)


a = A('ytyt', 8)
print(a)


##############################
class Interact:

    inter_1 = 55
    Inter_2 = 77

    def __init__(self, inter_int1: str, inter_int2: str):
        self.inter_1 = inter_int1
        self.Inter_2 = inter_int2

    def __str__(self):
        return "{}{}".format(self.inter_1, self.Inter_2)

    def class_meth(cls, new_value1, new_value2):
        print(Interact.inter_1, Interact.Inter_2)
        Interact.inter_1 = new_value1
        Interact.Inter_2 = new_value2


    def inst_meth(self):
        print(self.inter_1 + " " +self.Inter_2)

    def some_calc(self, sum1: int, sum2: int):
        formula = (sum1+sum2)/(sum1-sum2)
        print(formula)

###############################################################
inter = Interact('first argument', 'second argument')
inter.class_meth(123, 456)
print(Interact.inter_1, Interact.Inter_2)

################################################################
inter.inst_meth()

################################################################
inter.some_calc(6,50)
################################################################
inter.inter_1 = "changed argument"
inter.inst_meth()

################################################################
setattr(inter, 'inter_int3', 'third argument')
print(getattr(inter, 'inter_int3'))
