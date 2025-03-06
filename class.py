# class Cars:
#     def __init__(self,engine,torque):
#         self.engine=engine
#         self.torque=torque
#
#     def power(self):
#         print(f"The car has a {self.engine} engine and {self.torque} Nm of torque.")
from tkinter.font import names


# car1=Cars('v8',460)
# car2=Cars('v6',520)
#
# car1.power()
# car2.power()

# class Computer:
#     def __init__(self):
#         self.name="charan"
#         self.age=22
#
#     def update(self):
#         self.age=30
#
#     def compare(self,other):
#         if self.age==other.age :
#             return True
#         else:
#             return False
#
#
#
# c1=Computer()
# c2=Computer()
# c1.name="rakesh"
# c2.age=23
# c2.update()
#
#
# if c1.compare(c2):
#     print("same")
# else:
#     print("not same")
#
#
#
# print(c1.age)
# print(c2.age)
#
#
# print(id(c1))
# print(id(c2))

#
# class Car:
#     wheels = 4
#     def __init__(self):
#         self.name = "bmw"
#         self.mil=10
# car1=Car()
# car2=Car()
#
# car1.mil = 20
# car1.name = "bently"
#
# Car.wheels = 5
#
# print(car1.mil,car1.name,Car.wheels)
# print(car2.mil,car2.name,car2.wheels)

# class Student:
#     school = "snist" #class variable
#
#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3) / 3
#
#     @classmethod#CLASSMETHOD
#     def name(cls):
#         return cls.school
#
#     @staticmethod
#     def info():
#         print("located  in ghatkesar")# staticmethod
#
#
#
# s1=Student(12,13,14) #instance variable
# s2=Student(20,22,23) #instance variable
#
#
# print(s1.avg())
# print(s2.avg())
# print(Student.name())
# Student.info()


#inner class method

# class Student:
#     def __init__(self,name,number):
#         self.name=name
#         self.number=number
#         self.lap=self.Laptop()
#
#     def show(self):
#         print( f"my name is {self.name},and my roll number is {self.number}")
#         self.lap.show()
#
#
#     class Laptop:
#         def __init__(self):
#             self.brand="HP"
#             self.cpu="i5"
#
#         def show(self):
#             print( f"my laptop is {self.brand} and cpu is {self.cpu}")
#
#
#
# s1=Student("charan",22)
# s2=Student("sriya",21)
#
# s1.show()
# s2.show()


# class A:
#
#     def __init__(self):
#         print("charan")
#
#     def feature1(self):
#         print("feature 1 is workingg ")
#     def feature2(self):
#         print("feature 2 is working")
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("sriya")
#
#     def feature1(self):
#         print("feature 3 is workingg ")
#
#     def feature4(self):
#         print("feature 4 is working")
# a1=B()




# # a1 = A()
# # b1=B()
# # b1.feature2()
#
#
# class C(A,B):
#     pass
#     # def feature1(self):
#     #     print("feature5 is working")
# c1=C()
# # c1.feature1()
#












