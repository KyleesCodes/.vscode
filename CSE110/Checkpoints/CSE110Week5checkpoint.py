first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))
if first_number > second_number:
    print('The first number is greater.')
else:
    print('The first number is not greater.')
if first_number == second_number:
    print('The numbers are equal.')
else:
    print('The numbers are not equal.')
if first_number < second_number:
    print('The second number is greater.')
else:
    print('The second number is not greater.')

print('')

animal = input('What is your favorite animal? ')
if animal.lower() == 'panda':
    print('That is my favorite animal too!')
else:
    print('That is not my favorite animal.')
