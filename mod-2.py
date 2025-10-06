# num = int(input("Enter a number: "))

# if num % 2: print("Odd")

# else: print("Even")


#2.5
# price = 0
# age = int(input("Enter your age: "))

# if age in range(5):
#     ...

# elif age in range(6, 13):
#     price = 5

# elif age in range(13, 65):
#     price = 10

# else:
#     price = 7

# print(f"Price: £{price}")


#2.6
# light_color = input('Enter the colour of the traffic light: ').lower()

# if light_color == 'red':
#     print('Stop!')

# elif light_color == 'yellow':
#     print('Prepare to stop.')

# elif light_color == 'green':
#     print('Go!')

# else: 
#     print('Invalid light colour.')


#2.7
#Create variables: gpa (float, e.g., 3.8), extracurriculars (integer, e.g., 3), is_eligible_for_financial_aid (Boolean, e.g., True). 
#Use nested if statements to check for scholarship eligibility:
# First, check if gpa is 3.5 or higher.
# Inside that if block, check if extracurriculars is 2 or more.
# Inside that if block, check if is_eligible_for_financial_aid is True.
# If all conditions are met, print "Eligible for full scholarship!".
# Provide else statements for each level of nesting to explain why the student is not eligible (e.g., "GPA too low", "Not enough extracurriculars", "Not eligible for financial aid").

# gpa = 3.9
# extracurriculars = 4
# is_eligible_for_financial_aid = True

# if gpa >= 3.5:
#     if extracurriculars >= 2:
#         if is_eligible_for_financial_aid:
#             print("Eligible for full scholarship!")
        
#         else:
#             print("Not eligible for financial aid")
    
#     else:
#         print("Not enough extracurriculars")

# else:
#     print("GPA too low")


#2.8
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print(f'SUM: {num1 + num2}\nDIFF: {num1 - num2}\nPROD: {num1 * num2}\nQUO: {num1 / num2}')


#2.9
# sentence = input("Enter a sentence: ").strip()
# words = sentence.split(' ')
# print(len(words))

#2.10
# import math
# alt = float(input("Enter the height of the triangle: "))
# base = float(input('Enter the base of the triangle: '))
# hypo = math.sqrt(alt**2 + base**2)

# print(hypo)


def animal_speech(animal_type):

    if animal_type == 'dog':
        return 'Woof!'

    elif animal_type == 'cat':
        return 'Meow!'

    elif animal_type == 'bird':
        return 'Chirp!'
    
    elif animal_type == 'horse':
        return 'Neigh!'
    
    else:
        return None
    
# animal = input("Enter an animal type: ")

# print(animal_speech(animal))


#2.12
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# favorite_book("Monster")


#2.13
def make_shirt(size, message):
    print(f"You have ordered a shirt of size {size} with the message \"{message}\"")

# make_shirt("medium", "Chalo Jhola leke!")
# make_shirt(message="Chalo Jhola leke!", size="large")


#2.14
def city_country(city, country):
    return f'{city}, {country}'

# print(city_country('New Delhi', 'India'))
# print(city_country('London', 'United Kingdom'))
# print(city_country('Gaza', 'Palestine'))



#2.15
def make_album(artist, album_name, track = 1):
    return {"Album Name": album_name, "Artist": artist, "Tracks": track}

# print(make_album('Shaheer Ali', 'Fortuner Meri life...', 12))



#2.16
from datetime import datetime

def display_current_time():
    now = datetime.now()
    print(f'Current time: {now}')

# display_current_time()



#2.17
usernames = ['Muneer', 'Ali', 'Sharique']

def greeter(usernames):
    for user in usernames:
        print(f"Hello, {user}")

# greeter(usernames)

# usernames.append('Maaz')

# greeter(usernames)


#2.18
counter = 0

def add_to_counter():
    global counter
    counter += 1
    print(counter)

# add_to_counter()
# add_to_counter()
# add_to_counter()
# add_to_counter()
# add_to_counter()
# print(counter)


#2.19
def create_and_print_local():
    my_local_var = 'Hello'

    print(my_local_var)


# create_and_print_local()
# print(my_local_var)


#2.20
def display_welcome(name, language='English'):
    if language == 'English':
        print(f'Hello, {name}')
    
    elif language == 'Spanish':
        print(f'Hola, {name}')
    
    elif language == 'French':
        print(f'Bonjour, {name}')
    
    else:
        print(f'Welcome, {name}')

# display_welcome('Maria')
# display_welcome('Pierre', 'French')
# display_welcome('Liam', 'German')



#2.21
# from random import randint

# random_number = randint(1, 100)

# while True:
#     guess = int(input("Enter your guess: "))

#     if guess == random_number:
#         print('You guessed it!')
#         break
    
#     elif guess > random_number:
#         print('Too high!')
    
#     elif guess < random_number:
#         print('Too low!')



#2.22
# while True: 
#     topping = input("Enter a pizza topping ('quit' to exit): ")

#     if topping == 'quit':
#         break

#     else: 
#         print(f"Adding {topping} to your pizza!")

# print('Your pizza is being prepared!')


#2.23
# fav_fruits = ['Papuya', 'Banana', 'Strawberry', 'Watermelon', 'Guava', 'Grapes']

# for fruit in fav_fruits:
#     print(f"I love {fruit}")

# print('I really enjoy fruits!')



#2.24
# for i in range(1, 10):
#     if i % 3 == 0:
#         print(i)



#2.25
# while True:
#     num = int(input("Enter a positive number: "))

#     if num <= 0:
#         print('Invalid input. Please try again.')
#         continue
#     else:
#         print(f'You entered: {num}')
#         break



#2.26
# students = ["Anna", "Ben", "Chris", "Dana", "Ethan", "Frank"]

# for student in students:
#     if student == 'Chris' or student == 'Ethan':
#         print(f'Skipping {student} for now.')
    
#     else: 
#         print(f'Processing student: {student}')

#2.27
# balance = 1000

# while True:
#     action = input('1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\nChoose your action: ').lower()

#     if action == 'deposit':
#         amount = float(input('Enter an amount to deposit: $'))

#         if amount > 0:
#             balance += amount
#             print(f"${amount} successfully deposited.")
#             print(f"Balance: ${balance}")
        
#         else:
#             print('Invalid deposit amount.')

#     elif action == 'withdraw':
#         amount = int(input('Enter an amount to withdraw: $'))

#         if amount > 0 and amount <= balance:
#             balance -= amount
#             print(f"${amount} successfully withdrawn.")
#             print(f"Balance: ${balance}")
    
#         elif amount > balance:
#             print('Insufficient funds.')
        
#         else:
#             print('Invalid withdrawal amount.')

#     elif action == 'check balance':
#         print(f"Balance: ${balance}")

#     elif action == 'exit':
#         print('Thank you for banking with us!')
#         break

#     else:
#         print('Invalid option. Please try again')

#2.28
menu = {"pizza": 12.00, "pasta": 10.50, "salad": 7.00, "drink": 2.50}

def take_order():
    total_cost = 0

    while True:
        item = input('What would you like to order (done to exit): ')

        if item == 'done':
            break

        elif item in menu:
            total_cost += menu[item]
            
            print(f'Added {item} to your order. Current total: £{total_cost:.2f}')

        else:
            print(f"Sorry, {item} is not on the menu.")

    return total_cost

# total = take_order()

# print(f"Your final bill is: £{total:.2f}")


#2.29
def check_password_strenght(password):
    if len(password) < 8: 
        return "Weak: Password is too short."
    
    if password.upper() == password:
        return "Weak: Password needs lowercase letters."
    
    if password.isalpha():
        return "Weak: Password needs numbers or special characters."
    
    else:
        return "Strong"
    

# while True:
#     password = input("Enter a password: ")

#     return_value = check_password_strenght(password)

    # if return_value == 'Strong':
    #     print('Strong password.')
    #     break
    
#     else:
#         print(return_value)


#2.30
todo_list = []

def add_task(task):
    todo_list.append(task)
    print('Task added.')

def view_tasks():
    if todo_list == []:
        print("No tasks in the list.")
        return
    
    for i in range(len(todo_list)):
        print(f'{i + 1}. {todo_list[i]}')

def mark_task_complete(task_index):
    if task_index >= 1 and task_index <= len(todo_list):
        print(f"DONE: {todo_list[task_index-1]}")
        todo_list.pop(task_index - 1)

    else:
        print('Invalid task number')

def runner():
    options = '1. Add Task\n2. View Tasks\n3. Mark Task Complete\n4. Exit'
    
    while True:
        print(options)

        choice = input('Enter your choice: ').lower()

        if choice == 'add task':
            task = input('Enter task: ').lower().capitalize()
            
            add_task(task)

        elif choice == 'view tasks':
            view_tasks()

        elif choice == 'mark task complete':
            view_tasks()

            task_index = int(input('Enter the index of the task to mark complete: '))

            mark_task_complete(task_index)

        elif choice == 'exit':
            print('Goodbye!')
            return

        else: 
            print('Invalid choice.')
        
        print()

# runner()


#2.31
def generate_fibonacci(limit):
    fib_sequence = []
    a, b = 0, 1

    while a <= limit:
        fib_sequence.append(a)

        a, b = b, a + b

    return fib_sequence

limit = int(input('Enter the upper limit for fibonacci series: '))
print(generate_fibonacci(limit))


#example 
for i in range(1, 6):
    print('*'*i)

    