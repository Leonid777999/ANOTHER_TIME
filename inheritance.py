class Transport:

    def __init__(self, wheels: int, engine_type: str):
        self.wheels = wheels
        self.engine_type = engine_type

    def start_engine(self):
        push_pedal = int(input())
        if push_pedal >= 50:
            print("Fast")
        else:
            print("Slow")

    def stop_engine(self):
        pass

    def change_engine(self, new_engine_type):
        experimental_engine = self.engine_type + new_engine_type
        return experimental_engine


class Car(Transport):

    def __init__(self, wheels: int, engine_type: str, style: str):
        super().__init__(wheels, engine_type)
        self.style = style

    def change_style(self, new_style: str):
        saved_style = self.style
        self.style = new_style
        print("Previous style was {} and now it is {}".format(saved_style, new_style))

    def change_engine(self, new_engine_type: str):
        saved_engine = self.engine_type
        self.engine_type = new_engine_type
        print("Previuos engine was {} and new is {}".format(saved_engine, new_engine_type))


jeep = Car(4, 'gaz engine', 'crossover')


jeep.change_style('sedan')
print(jeep.style)

jeep.change_engine('electric engine')
print(jeep.engine_type)

jeep.start_engine()
###############################################################


class A:

    def __init__(self, a_parameter: int, aa_parameter: int):
        self.a = a_parameter
        self.aa = aa_parameter

    def aclass(self):
        print(self.a + self.aa)


class B:

    def __init__(self, b_parameter, bb_parameter):
        self.b = b_parameter
        self.bb = bb_parameter

    def aclass(self):
        print(self.b * self.bb)


class C(B,A):

    def __init__(self, b_parameter, bb_parameter):
        super().__init__(b_parameter, bb_parameter)


check_method = C(8,4)
check_method.aclass()







