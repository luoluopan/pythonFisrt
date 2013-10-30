# coding=gbk
__author__ = 'renfei'

class Person():
    ''' Represent any school member.
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def tell(self):
        ''' Tell my details.
        '''
        print("Name: %s Aage: %s" %(self.name,self.age))


class Teacher(Person):
    def __init__(self,name,age,salary):
        Person.__init__(self,name,age)
        self.salary = salary
        print("Initialized Teacher: %s" % self.name)
    def tell(self):
        Person.tell(self)
        print("Salary is %s" % self.salary)

t = Teacher("任飞","24","2000")
t.tell()

