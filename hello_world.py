#rock (1), scissors (2), paper (3)
import random
import sys

user_play = 0
comp_play = 0
user_score = 0
comp_score = 0
user_won = False

while True:
    if (user_score != 0 or comp_score != 0):
        print('')
        print('Current score:')
        print('Player: ' + str(user_score))
        print('Computer: ' + str(comp_score))

    print('Choose an opetion: rock (1), scissors (2), paper (3) (press 0 to exit)')

    try:
        user_play=int(input('  Choose from (1,2,3): '))
    except ValueError:
        print ('Not a number, try again!')
        continue

    if (user_play == 0):
        sys.exit(0)

    if (user_play < 1 or user_play > 3):
        print('Choose a value between 1 and 3')
        continue

    comp_play = random.randint(1, 3)

    if (user_play == comp_play):
        print('Par! Nobody wins, everybody loses!')
        continue

    if ((user_play == 1 and comp_play == 2) or
        (user_play == 2 and comp_play == 3) or
        (user_play == 3 and comp_play == 1)):
        user_won = True

    if (user_won):
        print('Congratulations you won!')
        user_score += 1
    else:
        print('I am sorry, you lost!')
        comp_score += 1
    
    user_won = False


        
