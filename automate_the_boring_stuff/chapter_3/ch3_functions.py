def helloBasic():
    print("Howdy!")
    print("Howdy!!")
    print("Hello There!")
"""
helloBasic()
helloBasic()
helloBasic()
"""

def helloInputName(name):
    print("Hello " + name)

"""
helloInputName("Alice")
helloInputName("Bob")
"""

#keyword arguments and the print(function)
#prints the words together as: HelloWorld
print("Hello", end="")
print("World")

#similar effect
print('cats', 'dogs', 'mice') #prints cats dogs mice
print('cats', 'dogs', 'mice', sep=',') #prints cats,dogs,mice