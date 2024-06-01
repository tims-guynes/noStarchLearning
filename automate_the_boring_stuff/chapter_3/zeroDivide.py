#this will error
def spamError(divideBy):
    return 42/divideBy
"""
print(spamError(2))
print(spamError(14))
print(spamError(12))
print(spamError(1))
print(spamError(0))
"""

#exception handling
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(spam(2))
print(spam(14))
print(spam(12))
print(spam(1))
print(spam(0))