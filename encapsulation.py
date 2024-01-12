class Encapsulate:

    def __init__(self, protected="protected_old", private="private_old"):
        self._protected = protected
        self.__private = private

    def __str__(self):
        return str(self._protected), str(self.__private)

    def usual_method(self):
        print("Method is running", self._protected, self.__private)

    def _protected_method(self):
        return self.__dict__

    def __private_method(self):
        return self.__dict__


class EncapsulateJunior(Encapsulate):

    def __init__(self, protected, private, public):
        super().__init__(protected, private)
        self.public = public

###################################################


encap = Encapsulate("protected", "private")
print(encap._protected)
print(encap._Encapsulate__private)

encap._protected = "protected1"
encap._Encapsulate__private = "private1"
print(encap._protected)
print(encap._Encapsulate__private)

#######################################################

encap_jun = EncapsulateJunior("protected_jun", "private_jun", "public")

print(encap_jun._protected_method())
encap_jun.usual_method()
print(encap_jun._protected)
print(encap_jun._Encapsulate__private)


