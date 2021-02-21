import random

print('Hello. What is your name')
name = input()
sNum = random.randint(1,20)

print('Well, ' + name + ', I am thinking of a number between 1 and 20')
print('Take a guess.')

for count in range(1,7):
    guess = int(input())
    if guess > sNum:
        print('Your guess is too high.')
    elif guess < sNum:
        print('Your guess is too low.')
    else:
        break;
if guess == sNum:
    print('You got it ' + str(sNum) + ' was the secret number.')
else:
    print('Nope. The number i was thinking about was ' + str(sNum))

    



