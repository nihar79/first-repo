class Denominations:
    def __main__(self):
        amount=int(input("Enter the Amount "))
        notes=self.denominations(amount)
        print("500--->",notes[0])
        print("50---->",notes[1])
        print("10---->",notes[2])
        print("1----->",notes[3])

    def denominations(self,amount):
        notes=[0,0,0,0]
        a=amount//500
        notes[0]=a
        amount=amount-a*500
        b=amount//50
        notes[1]=b
        amount=amount-b*50
        c=amount//10
        notes[2]=c
        amount=amount-c*10
        d=amount//1
        notes[3]=d
        return notes
    
ob=Denominations()
ob.__main__()