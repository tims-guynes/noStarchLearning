import time, sys
indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # pause for 1/10 of a second

        if indentIncreasing:
            # Increaste the number of spaces:
            indent = indent + 1
            if indent == 20:
                # change direction
                indentIncreasing = False
        else:
            # decrease the number of spaces
            indent = indent -1
            if indent == 0:
                #change direction
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()