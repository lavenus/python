#-*- coding: UTF-8-*-
# Question Game:程序开始时，在0~100之间生成一个随机数，这个数是对用户隐藏的。
#               然后用户尝试猜测这个数，程序给出猜测方向(更大或更小，更高或更低)
#               的提示，用户继续进行猜测。游戏以两种方法之一结束：
#               (1)用户猜中数字。
#               (2)用户通过输入0~100范围外的数字，退出游戏。
# 
# Chinese Arithmetic:
#       (1).选择一个随机数。
#       (2).提示用户进行猜测。
#       (3).while猜测的数字在0~100范围内：
#       (4).检查猜测结果是否正确，如果正确，显示获胜消息并退出。
#       (5).否则,给出提示,并提示进行新的猜测.

# English Arithmetic:
#       (1).while-else
#       (2).Simple guessing game: start with a random number and
#       (3).guess with hints until:
#       (4).guess is correct
#       (5).the guess is out of range indication the user is quitting

import random # get the random number module
number = random.randint(0,100) # get a random number
                               # between 0 and 100 inclusive

print "Hi-Lo Number Guessing Game: between 0 and 100 inclusive."
print

#get and initial guess
guessString = raw_input("Guess a number: ")
guess = int(guessString) # convert string to number

# while guess is range, keep asking
while 0 <= guess <=100:
    if guess > number:
        print "Guessed Too High."
    elif guess < number:
        print "Guessed Too Low."
    else:               # correct guess, exit with break
        print "You guessed it. The number was:",number
        break
    # keep going,get the next guess
    
    guessString = raw_input("Guess a number: ")
    guess = int(guessString)
else:
    print "You quit early, the number was:",number
