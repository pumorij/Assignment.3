# Q1

from doctest import OutputChecker


def a_fun():
    global name
    name = 'A'
def b_fun():
    global name
    name = 'B'
b_fun()
a_fun()
print (name)

# Output
# A