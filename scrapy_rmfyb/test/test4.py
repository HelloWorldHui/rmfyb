# coding=utf
"""
author=Hui_T
"""
print('\xa0')


class A():
    data = '1'

    def x(self):
        self.data = '2'

    def f(self):
        print(self.data)


a = A()
# a.f()
a.x()
a.f()  # 2
print(a.data)  # 2
print(A.data)  # 1
