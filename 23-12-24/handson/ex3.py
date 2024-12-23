class OutOfRangeError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Average:
    def input_marks(self):
        try:
            a=int(input("Subject A Marks "))
            b=int(input("Subject B Marks "))
            c=int(input("Subject C Marks "))
        except ValueError as e:
            print("Please enter an appropriate value")
            return None
        except Exception as e:
            print("Please enter an appropriate value")
            return None
        return a,b,c
    
    def avg_marks(self):
        try:
            a1,b1,c1=self.input_marks()
            a2,b2,c2=self.input_marks()
        except TypeError as e:
            print("Exiting due to invalid input...")
            return None
        try:
            self.in_range(a1,b1,c1,a2,b2,c2)
        except OutOfRangeError as o:
            print(o.args[0])
            return None
        
        print("Average marks for student A", self.average(a1,b1,c1))
        print("Average marks for student B", self.average(a2,b2,c2))
    
    def average(self,a,b,c):
        return (a+b+c)//3

    def in_range(self,a1,b1,c1,a2,b2,c2):
        if a1 < 0 or a1 > 100 or b1 < 0 or b1 > 100 or c1 < 0 or c1 > 100:
            raise OutOfRangeError("Marks should be between 1-100")
        if a2 < 0 or a2 > 100 or b2 < 0 or b2 > 100 or c2 < 0 or c2 > 100:
            raise OutOfRangeError("Marks should be between 1-100")

ob = Average()
ob.avg_marks()