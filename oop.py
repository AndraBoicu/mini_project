# # #
# # # # def hello():
# # # #     print('hello')
# # #
# # # # x=1
# # # # y='hello'
# # # # print(x+y)
# # #
# # # # string='hello'
# # # # print(string.upper())
# # #
# # # class Dog:
# # #     def __init__(self, name, age):
# # #         self.name=name
# # #         self.age=age
# # #         # print(name)
# # #
# # #     # def add_one(self, x):
# # #     #     return x+1
# # #     #
# # #     # def bark(self):
# # #     #     print('bark')
# # #
# # #     def get_name(self):
# # #         return self.name
# # #
# # #     def get_age(self):
# # #         return self.age
# # #
# # #     def set_age(self, age):
# # #         self.age=age
# # #     def set_name(self, name):
# # #         self.name=name
# # #
# # # # d=Dog()
# # # # d.bark()
# # # # print(d.add_one(5))
# # # # print(type(d))
# # # d=Dog('tim', 5)
# # # d.set_age(9)
# # # print(d.get_age())
# # # # d2=Dog('bill', 3)
# # # # print(d2.get_age())
# #
# # #OOP
# #
# # class Dog:
# #     def __init__(self, name, color):
# #         self.name=name
# #         self.color=color
# #
# #     def get_name(self):
# #         return self.name
# #     def get_color(self):
# #         return self.color
# #     def set_name(self, name):
# #         self.name=name
# #     def set_color(self,color):
# #         self.color=color
# #
# # d=Dog("bibi","blue")
# #
# # d.set_name("bibibi")
# # print(d.get_name())
# # d.set_color("red")
# # print(d.get_color())
#
# #OOP
#
# # class Student:
# #     def __init__(self, name, age, grade):
# #         self.name=name
# #         self.age=age
# #         self.grade=grade #0-100
# #
# #     def get_grade(self):
# #         return self.grade
# #
# # class Course:
# #     def __init__(self, name, max_students):
# #         self.name=name
# #         self.max_students=max_students
# #         self.students=[]
# #
# #     def add_student(self, student):
# #         if len(self.students)<self.max_students:
# #             self.students.append(student)
# #             return True
# #         return False
# #
# #     def get_average_grade(self):
# #         value=0
# #         for student in self.students:
# #             value+= student.get_grade()
# #         return value/len(self.students)
# #
# #
# #
# # s1=Student('tim',20,80)
# # s2=Student('bill',22,95)
# # s3=Student('jill',19,70)
# #
# # course=Course("Science",2)
# # course.add_student(s1)
# # course.add_student(s2)
# # print(course.students[0].name)
# # print(course.get_average_grade())
#
#
# #OOP7
#
# class Students:
#     def __init__(self, name, age, grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#
#     def get_grade(self):
#         return self.grade
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name=name
#         self.max_students=max_students
#         self.students=[]
#
#     def add_student(self, student):
#         if len(self.students)<self.max_students:
#             self.students.append(student)
#             return True
#         return False
#     def average(self):
#         value=0
#         for student in self.students:
#             value+=student.get_grade()
#         return value/len(self.students)
#
# s1=Students('bill', 20, 80)
# course=Course("Science", 2)
# course.add_student(s1)
# print(course.students[0].name)
