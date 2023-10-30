    class Student: amount_of_students = 0
    def __init__ (self,height = 160):
        self.height = height
        self.money = 2000;
        Student.amount_of_students += 1

    1 usage
    def printHeight(self):
    print(self.height)
    2 usages
    def printCountMoney(self):
        print(self.money)
    2 usages
    def subMoney(self, countMoney = 0):
        self.money = countMoney
        Student.printCountMoney(self)

stepan = Student (height=180)
stepan.printHeight()
stepan.printCountMoney()
print("-"*20)

katrin = Student (height=170) # katrin.printCountMoney() katrin.subMoney (200)
# katrin.printCountMoney()
print("-"*20)

oleg = Student(height=190)
oleg.printHeight()
oleg.printCountMoney
print("-"*20)