__author__ = 'renfei'

class Person():
    def __init__(self,name):
        self.name = name

    def sayHello(self):
        print("hello,everbody!")

    def sayGood(self,userName):
        print("you are good man %s" % userName)

    def sayInit(self):
        print("init hanshu de canshu %s" % self.name)


#p = Person()
#p.sayHello()
#p.sayGood("renfei")

p1 = Person("Swaroop")
p1.sayInit()
