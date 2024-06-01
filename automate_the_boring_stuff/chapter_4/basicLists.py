# a place to learn about lists
intList01 = [1, 2, 3, 4, 5, 6]

stringList01 = ['cat', 'dog', 'bird', 'fish', 'yourmom']
stringList02 = ['mouse', 'cat', 'dog', 'elephant']

mixedList01 = ['blegh', 3.14159, 'your moms mom', 5, True, None, 42]

multiListList01 = [['tabby', 'seal point'], [1, 2, 3, 5, 8]]

#basic calls
print('-------------- Basic calls')
print(intList01[1]) # returns 2
print(stringList01[3]) # returns 'fish'

#negative reference
print("")
print('-------------- Negative calls')
print(mixedList01[-1])
print(f"The {stringList02[-1]} is afraid of the {stringList02[-4]}.")

#list list reference
print("")
print('-------------- List List refence')
print(multiListList01[1][3]) # returns 5
print(multiListList01[0][1]) # returns seal point

#slicking list
print("")
print('-------------- List List refence')
print(stringList01[1:3])