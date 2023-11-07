# # class Parent:
# #     pass
# #
# # class Child(Parent):
# #     pass
# #
# # class Human:
# #     height = 170;
# #
# # class Student(Human):
# #     salary = 400
# #
# # class Worker(Human):
# #     salary = 15000
# #
# # nick = Student()
# # Anna = Worker()
# # print(nick.height)
# # print(nick.salary)
# # print("----")
# # print(Anna.height)
# # print(Anna.salary)
# #
# #
# #
# # class GrandParent:
# #     height = 170
# #     satiety = 100
# #     age = 60
# #
# # class Parent(GrandParent):
# #     height = 170
# #     age = 40
# #
# # class Child(Parent):
# #     height = 50
# #     def __init__(self):
# #         print(self.height)
# #         print(self.satienty)
# #         print(self.age)
# # nick = Child()
#
#
#
#
#
#
#
#
#
#
#
# class Hello:
#     def __init__(self):
#         print("hello")
# class HelloWorld(Hello)
#     def __init__(self):
#         super().__init__()
#         print("World")
# one = HelloWorld()


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

Jamal = Child()