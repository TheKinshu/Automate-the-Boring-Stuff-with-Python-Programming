import logging

logging.basicConfig(filename='.\\Debugging\\myProgram.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('The return value is %s' % (total))

    return total

print(factorial(5))

logging.debug('End of program')

# logging.disable(logging.CRITICAL)
# logging.debug is helpful in many cases, they do precisely what print do and gives timestamp of the debug - 
# it also has a feature that allow you to disable all logging. Allowing you to save time without deleting/commenting
# print function out.


# Theres 5 level of debug.
# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical

# Each one of those level disable that level and the level(s) below it
# Disabling only a certain part of the logging can be helpful. It allows-
# users to keep tracks of critical part of the program.


# You can also log the debugs into a file by adding filename into the config
# logging.basicConfig(filename='myProgram.txt' level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
