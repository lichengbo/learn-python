# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)


student = Student('cbli', 99)
student.name = 'aaa'
student.print_score()
print student.get_name()
print dir(student)