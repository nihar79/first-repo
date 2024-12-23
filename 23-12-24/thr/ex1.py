from threading import Thread
from time import sleep

class Sample(Thread):
    def m1(self):
        for i in range(1,21):
            print(i)
            sleep(1)
            
    def run(self):
        self.m1()

class Demo(Thread):
    def m2(self):
        for i in range(21,41):
            print(i)
            sleep(1)

    def run(self):
        self.m2()

ob1 = Sample()
ob2 = Demo()
ob1.start()
ob2.start()
ob1.join()
ob2.join()
print("End of Program")