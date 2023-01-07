
# Enjoy my Grade Generator

test = input ('Type in the name of the test: ')
maxscore = float(input ('Type in the maximun score you could receive: '))
testscore = float(input ('How many points you received? '))

var2 = round(float((testscore * 100) / maxscore),2)
print('Your test result is:', var2, '%!')

if var2 >= 90 :
    print('Congratulations, you got A+!')
elif var2 >= 80 and var2 <= 89 :
    print('Congratulations, you got A!')
elif var2 >= 70 and var2 <= 79 :
    print('Congratulations, you got B!')
elif var2 >= 60 and var2 <= 69 :
    print('Congratulations, you got C!')
elif var2 >= 50 and var2 <= 59 :
    print('Congratulations, you got D!')
else:
    var2 <= 49
    print('Keep studying, you got E!')
