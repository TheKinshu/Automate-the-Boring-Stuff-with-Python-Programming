"""


**************************
*                        *
*                        *
*                        *
**************************


"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to a string of length 1.')

    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5)


import traceback

try:
    # Raise your own exceptions
    raise Exception('This is the error message.')
except:
    errorFile = open('.\\Debugging\\error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback infor was written to error_log.txt')

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            print(intersection[key])
            intersection[key] = "yellow"

        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
        print(intersection[key])
    # Assertions are for decting programmer errors that are not meant to be reccovered from.
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)


print(market_2nd)
switchLights(market_2nd)
print(market_2nd)