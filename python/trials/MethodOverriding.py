#!/usr/bin/python
class Parent:
    def myMethod(self):
        print("Its Parent Method")

class Child(Parent):
    def myMethod(self):
        print("Hey I am overriding parent method")

child =Child()
child.myMethod()
