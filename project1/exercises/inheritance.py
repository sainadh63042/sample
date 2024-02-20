class SuperClass:
    def super_class_method(self):
        print("Hi, This is super class.")


class ChildClass(SuperClass):
    def child_class_method(self):
        print("Hi, This is child class.")


obj = ChildClass()
obj.super_class_method()
obj.child_class_method()
