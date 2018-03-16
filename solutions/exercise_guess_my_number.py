low = 0
high = 100
input_user = ''
print("Please think of a number between 0 and 100!")
while input_user != 'c':
    ans = (low + high) // 2
    print('Is your secret number ', end='')
    print(ans, end='')
    print('?')
    input_user = input('Enter \'h\' to indicate the guess is too high. '
                       'Enter \'l\' to indicate the guess is too low. '
                       'Enter \'c\' to indicate I guessed correctly. ')
    if input_user not in 'chl':
        print('Sorry, I did not understand your input.')
        continue
    if input_user == 'c':
        print('Game over. Your secret number was: ', end='')
        print(ans)
        break
    if input_user == 'h':
        high = ans
    if input_user == 'l':
        low = ans
