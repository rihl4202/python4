class Atm:
    def __init__(self,num,pin):
        self.num = num
        self.pin = pin
    def balance(self):
        print("Your balance is 87. ")
    def withdraw(self,value):
        new = 87-value
        print("Your new balance is ",new)

atm1 = Atm(28,20)
print(atm1.num)
atm1.balance()
atm1.withdraw(5)