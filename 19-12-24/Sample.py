class Sample:
    a=10
    name="Python"

    def m1(self):#<----|
        print("m1")#   |
    #                  |
    def m2(self):#     |
        print("m2")#   |
#                      |
obj1=Sample()#         |
#                      |
print(obj1.a)#         |
obj1.m1() #m1(obj1)----|

