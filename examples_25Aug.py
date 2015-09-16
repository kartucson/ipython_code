__author__ = 'karthik'


from numpy.random import randn

data = {i :randn() for i in range(7)}

print data

problem here

data = {i :randn() for i in range(10)}

print data


class Message:
    def __init__(self,msg):
        self.msg = msg
    def __repr__(self):
        return 'Message: %s' % self.msg

x = Message('What is happening')
x
