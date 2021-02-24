# Return as a single string
helloFile  = open('E:\\Study\\AutomateCourse\\files\\hello.txt')
content = helloFile.read()
helloFile.close()

# Readline returns a list of string 
helloFile  = open('E:\\Study\\AutomateCourse\\files\\hello.txt')
content = helloFile.readlines()
helloFile.close()


#
helloFile  = open('E:\\Study\\AutomateCourse\\files\\hello2.txt', 'w')
helloFile.write('Hello!!!!!!')
helloFile.write('Hello!!!!!!')
helloFile.write('Hello!!!!!!')
helloFile.close()

baconFile = open('E:\\Study\\AutomateCourse\\files\\bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable and it\'s great.')

baconFile.close()

baconFile = open('E:\\Study\\AutomateCourse\\files\\bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious.')

baconFile.close()

import shelve
shelfFile = shelve.open('E:\\Study\\AutomateCourse\\files\\mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('E:\\Study\\AutomateCourse\\files\\mydata')
shelfFile.keys()
print(list(shelfFile.keys()))
print(list(shelfFile.values()))