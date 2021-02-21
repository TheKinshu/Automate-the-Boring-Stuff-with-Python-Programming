def test():
    print('Type 1 or 2')
    tempNum = input()
    try:
        if int(tempNum) == 1:
            print('You enter 1')
        elif int(tempNum) == 2:
            print('You enter 2')
    except ValueError:
        print('You did not enter a number!')

test()
