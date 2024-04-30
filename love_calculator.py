print('Welcome to the Love Calculator!')
name1 = input("What is your name : ").lower()
name2 = input('What is the name of your crush: ').lower()

combined_names = name1 + name2
print(combined_names)
count = 0
count += combined_names.count('t')
count += combined_names.count('r')
count += combined_names.count('u')
count += combined_names.count('e')
print(count)

count_1 = 0
count_1 += combined_names.count('l')
count_1 += combined_names.count('o')
count_1 +=  combined_names.count('v')
count_1 += combined_names.count('e')
print(count_1)

#Love calculaor
love_cal = str(count) + str(count_1)
print(love_cal)
love_calculator = int(love_cal)
print(love_calculator)

if love_calculator < 20 or  love_calculator> 90:
    print('Oops! Its unfortunate '+ name1.capitalize()+',' + ' You and your crush ' + name2.capitalize() + ' are not match afterall')
    print(f'Here is your score : {love_calculator}%')
elif love_calculator >= 40 and love_calculator<= 50:
    print('Yeyy!' + name1.capitalize()+',' + ' You and your crush ' + name2.capitalize() + ' are a perfect match')
else:
    print(f'Your love score with your crush is {love_calculator}%')
    print('Give it a try!')












