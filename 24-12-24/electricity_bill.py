class Electricity_Bill:
    def __main__(self):
        units=int(input("Enter the Number of units consumed "))
        bill=self.calculate_bill(units)
        print("You have to pay Rs",bill,"for electricity")
    
    def calculate_bill(self,units):
        if units <=50:
            bill=2*units
        elif units > 50 and units <= 150:
            bill=(2*50)+(units-50)*3
        elif units > 150 and units <= 250:
            bill=(2*50)+(3*100)+(units-150)*5
        elif units>250:
            bill=(2*50)+(3*100)+(5*100)+(units-250)*5

        #surcharge
        bill=bill+0.2*bill
        return bill
    
ob=Electricity_Bill()
ob.__main__()