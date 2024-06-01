def collatz():


    while True:
        try:
            number = int(input("please enter a number: "))
        except ValueError:
            print("Please enter a valid integer!")
        
        while True:
            if number == 1:
                print(int(number))
                break     
            if int(number) % 2 == 0:
                number = number / 2
                print(int(number))
            if int(number) % 2 == 1:
                if number == 1:
                    break
                number = (number * 3) + 1
                print(int(number))
        
    

collatz()