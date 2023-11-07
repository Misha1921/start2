class GrandParent:
    def about(self):
        print("I am GrandParent")

    def AboutMyself(self):
        print("I an=m GrandParent")

class Parent(GrandParent):
    def AboutMyself(self):
        print("I am parent")

class Child(Parent):
    def __init__(self):
        super().About()
        super().AboutMyself()

Jamil = Child()