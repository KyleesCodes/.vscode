print('Please enter the following information:')
print('')
print('')
first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email address: ')
phone_number = input('Phone number: ')
job = input('Job title: ')
id_number = input('ID number: ')
hair = input('Hair color: ')
eye = input('Eye color: ')
month = input('Name of start month: ')
training = input('Have you completed advanced training? Yes or no: ')
print('')
print('The ID card is:')
print('----------------------------------------------------')
print(last_name.upper() + ', ' + first_name.capitalize()) 
print(job.title())
print('ID: ' + id_number)
print('')
print(email.lower())
print(phone_number)
print('')
print(f"Hair: {hair:15} Eyes: {eye}")
print(f"Month: {month:14} Training: {training}")
print('----------------------------------------------------')
