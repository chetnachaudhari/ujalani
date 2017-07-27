#!/usr/bin/python

class Parent:
    parentAttr = 100
    def __init__(self):
        print("Calling Parent Constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Value of parent attribute is %d" % Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")

parent = Parent()
child = Child()
child.childMethod()
child.parentMethod()
child.getAttr()
child.setAttr(200)
child.getAttr()

print("Child is subclass of Parent" ,issubclass(Child, Parent))
print("parent is instance of Parent class",isinstance(parent, Parent))
print("parent is instance of Child class",isinstance(parent, Child))
print("child is instance of Parent class",isinstance(child, Parent))