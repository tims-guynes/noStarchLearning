import random

def getAnswer(num):
    if num == 1:
        return "It's decidely so"
    elif num == 2:
        return "Decidely So"
    elif num == 3:
        return "Yes"
    elif num == 4:
        return "Reply is hazy, please try again"
    elif num == 5:
        return "Ask later"
    elif num == 6:
        return "Ask again"
    elif num == 7:
        return "No"
    elif num == 8:
        return "Outlook does not look good"
    elif num == 9:
        return "Very Doubful"

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)