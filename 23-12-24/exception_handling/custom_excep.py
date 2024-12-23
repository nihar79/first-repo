class EligibleError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Sample:
    def test(self,age,percentage):
        if age<=17 or percentage<=60:
            raise EligibleError("Not eligible for registration")
        else:
            print("Registration Success")

obj1=Sample()
try:
    obj1.test(16,67)
except EligibleError as e:
    print(e.args[0])

print("End")