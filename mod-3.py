# #3.1
# favorite_language = 'Python'
# print(favorite_language)

# favorite_language = "Javascript"
# print(favorite_language)


# #3.2
# python_overview = \
# '''
# Easy to learn
# Powerful libraries
# Versatile
# '''
# print(python_overview)


# # 3.3
# word1 = "Python"
# word2 = "is"
# word3 = "fun"
# sentence = word1 + ' ' + word2 + ' ' + word3

# print(sentence)


# #3.4
# character = input('Enter a chr (*, -, = etc): ')

# print(character * 20)


# #3.5
# my_name = 'John Doe'
# print(my_name[0])
# print(my_name[-1])



# #3.6
# short_word = 'bug'
# print(short_word[3]) # IndexError: string index out of range


# #3.7
# email = 'student@example.com'

# for i in range(len(email)):
#     if email[i] == '@':
#         print(f"Domain: {email[i+1:]}")
#         break

# #3.8
# dirs = ['home', 'user', 'documents', 'project']
# path = '/'.join(dirs)

# print(path)

# #3.9
# user_input = ' PyThOn PrOgRaMmInG '.lower().strip()
# print(user_input)

# #3.10
# tags_str = 'python, programming, tutorial, beginners'
# tags_list = tags_str.split(', ')

# print(tags_list)


# # 3.11
# product_name = 'Smartphone'
# quantity = 2

# print(f"You have ordered {quantity} unit(s) of {product_name}.")


# #3.12
# event_title = 'Python Workshop'
# event_data = "2024-10-26"

# print("The event '{}' is scheduled for {}".format(event_title, event_data))


# #3.13
# name = input("Enter your name: ").lower().title().strip()
# age = int(input('Enter your age: '))

# print(f'Hello, {name}!', end=' ')

# if age >= 0 and age < 18:
#     print('You are a minor.')

# elif age >= 18 and age <= 25:
#     print('You are a young adult.')

# elif age > 25:
#     print('You are an adult.')

# else:
#     print('\nInvalid age.')


# #3.14
# sentence = input('Enter a sentence: ').strip()

# print(sentence.upper())
# words = sentence.split(' ')

# print(f'First word: {words[0]}\nLast word: {words[-1]}')


# #3.15
# noun = input("Enter a noun: ").title().strip()
# occupation = input('Enter an occupation of the noun: ').lower().strip()
# adjective = input('Enter an adjective for the noun: ').lower().strip()
# verb = input('Enter a verb for the noun: ').lower().strip()

# print(f"The {adjective} {occupation}, {noun}, {verb} across the lands.")


#3.16
# password = input('Enter a passoword: ')

# if len(password) < 8:
#     print('Weak: Password too short.')

# elif len(password) <= 12:
#     print("Moderate: Password length is okay.")

# else: 
#     print('Strong: Good password length!')

# if 'password' in password.lower():
#     print("Warning: Do not use 'password' in your password!")


# #3.17
# grocery_list = ['milk', 'eggs', 'butter', 'fruits', 'potato']

# print('Your Shopping List:')
# for i in range(len(grocery_list)):
#     print(f'\t{i + 1}. {grocery_list[i].title()}')


#3.18
# sen = list(input('Enter a sentence: ').strip())
# censor = (input("Enter a word to censor: "))

# for i in range(len(sen)):
#     if ''.join(sen[i:i+len(censor)]).lower() == censor.lower():
#         sen[i:i+len(censor)] = '*'*len(censor)

# print(*sen, sep='')