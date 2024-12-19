class Mobile1:
    def camera(self):
        print("40MP")
    def storage(self):
        print("128GB")

class Mobile2(Mobile1):
    def display(self):
        print("Curved Display")
    def storage(self):
        super().storage()

obj1 = Mobile2()
obj1.camera()
obj1.storage()