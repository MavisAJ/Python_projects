#Generate a password for your app using my code
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
           's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L',
           'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print('Welcome to my PyPassword Genrator!')

#Taking inputs for number of letters, symbols and numbers user wants in their password
nr_letters = int(input('How many letters would you like in your password\n'))
nr_symbols = int(input('How many symbols do you want in your password\n'))
nr_number = int(input('How many number do you want in your password\n'))

# password generator that shuffling 
# create a list out of the input since the shuffle func takes a list 
password = []
for let in range(0,nr_letters):
    password.append(random.choice(letters))
print(password)
for num in range(0,nr_number):
    password.append(random.choice(numbers))
print(password)
for num in range(0,nr_symbols):
    password.append(random.choice(symbols))
print(password)

#Use the shuffle function to join and shuffle password
random.shuffle(password)
# printing list of characters that shuffles for password
print(password)
#Joining the list back to a string to give us final password
password = ''.join(password)
print('Your password is ' + password)

# password generator without shuffling 
# password = ''
# for let in letters:
#     add1= nr_letters* random.choice(letters)
# password += add1
# print(password)

# for num in numbers:
#     add2 =nr_number* random.choice(numbers)
# print(add2)
# password +=add2
# print(password)
# for sym in symbols:
#     add3 =nr_symbols* random.choice(symbols)
# print(add3)
# password +=add3
# print(password)
# print('Your password is ' + password)