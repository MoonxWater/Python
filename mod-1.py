#1.1
_name = "name"
total_amount = 10
# class = 10 # this is not a valid name because class is a reserved keyword in python
user_id_123 = 123
# item#count = 10 # this is not valid because var names cannot have special characters except _

#1.2
city_name = "Patna"
active_users = 5000
is_administrator = True
product_price = 450

#1.3
'''
def, if, and, return, else, None, try, is, not, except, finally
'''

#1.4
# for = 15 # this throws syntax error as 'for' is a built-in keyword in python and when the interpreter reads the word, it looks for a valid for syntax

#1.5
result = 15 * 3 # this is an expression and a statement
"python is fun" # this is none
print('Coding...') # this is a statement
# if temperature > 25: this is both because the logical evaluates and gives back a value and depending on the value, some action is performed
# fahrenheit = celsius * 9/5 + 32 # this is an expression and a statement

#1.6
greeting = "Hello " + 'Python '
times = 3
print(greeting * times)

#1.7
city_name = "Mumbai"
population = 15000000
is_capital = False

print(f'City: {city_name}; Population: {population}; Capital: {is_capital}')

#1.8
count = 5
count = 10
double_count = count * 2

print(count, count, double_count)

#1.9
# 10 - 4 / 2 = 8
#(10 - 4) / 2 = 3
#3 ** 2 + 5 % 2 = 10
#x = 7; x //= 3 # this should print 2
# age = 20; has_license = True; # prints True
# print(age > 18 and has_license)


#1.10
# result = (5 ** 3 - 4) ** 0.5 + 15 / 5 < 11 and True
# print(result)


#1.11
fav_movie = "Ferdinand" # string
current_year = 2025 # int
rating = 3.6 # float
light_on = True # boolean
fav_colours = ['black', 'lava red', 'sian']
student_data = {'Name': "Muneer", 'Age': 19}

print(fav_movie)
print(type(fav_movie))
print(current_year)
print(type(current_year))
print(rating)
print(type(rating))
print(light_on)
print(type(light_on))
print(fav_colours)
print(type(fav_colours))
print(student_data)
print(type(student_data))


#1.12
first_word = "Python"
second_word = "Programming"
full_phrase = first_word + ' ' + second_word
print(full_phrase)
print(full_phrase * 3)
full_phrase = first_word + '\n\t' + second_word
print(full_phrase)


#1.13
temperature = 28
if temperature > 25:
    print("It's hot outside!")
    print("Consider staying hydrated.")

else: 
    print("It's a pleasant day.")

#1.14
if [] or 1:
    print('Hello World!')
    print("This is Python code executed by the if block.")

else:
    print("This code was executed by the else block.")



#1.15
#assign base variables
item_cost = 50
tax_rate = 0.08
shipping_fee = 5

#calculate tax and cost using values of base variables
total_before_tax = item_cost + shipping_fee
total_cost = total_before_tax * (1 + tax_rate)

#print the values of the variables in a good manner
print(f"Item: £{item_cost:.2f}")
print(f"Shipping: £{shipping_fee:.2f}")
print(f"Tax ({tax_rate*100}%): £{(item_cost + shipping_fee) * tax_rate:.2f}")
print(f"Total: £{total_cost:.2f}")


#1.16
def add(a, b):
    '''
    Adds two numbers and returns their result
    '''
    return a + b

add(5, 6)



#1.17
# name = input("Enter your name: ")
# fav_colour = input("Enter your favorite colour: ")
# lucky_number = int(input("Enter your lucky number: "))

# print(f"Name: {name}; Favourite Colour: {fav_colour}; Lucky Number: {lucky_number}")



#1.18
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 // num2)



#1.19
item = "Book"
quantity = 3
price = 12.50

print(f"You have {quantity} {item}(s) in your cart. Each {item} costs £{price}.")


#1.20
print(1, 2, 3, 4, 5, sep=', ', end='\nEnd of sequence.')



#1.21
# current_year = 2025
# birth_year = int(input("Enter your year of birth: "))

# print(f"Age: {current_year - birth_year} years old")


#1.22
item_count = 10
unit_price = 5.99

item_count = str(item_count)
unit_price = str(unit_price)

print("You ordered " + item_count + " items at £" + unit_price + " each.")



#1.23
favourite_number = 7
gpa = 3.8
is_member = False
name_list = ["Anna", "Ben"]

print(type(favourite_number))
print(type(gpa))
print(type(name_list))



#1.24
num_a = 5
num_b = 5
str_a = "hello"
str_b = "hello"
list_a = []
list_b = []
list_c = list_a

comparisons = [(num_a, num_b), (str_a, str_b), (list_a, list_b), (list_a, list_c)]

for item in comparisons:
    print(f"{item[0]} == {item[1]}: {item[0] == item[1]}")
    print(f"{item[0]} is {item[1]}: {item[0] is item[1]}")



#1.25
my_data = 25
print(my_data)
print(type(my_data))

my_data = "Python"
print(my_data)
print(type(my_data))

my_data = True
print(my_data)
print(type(my_data))



#1.26
list_eg = [1, 2, 3, 4, 5]
string = '5'
num = 6

# print(list_eg + num)
# print(string + num)

print(list_eg.append(num))
print(int(string) + num)



#End of Mod-1 Exercises
#1
name = input("Enter your name: ")
hobby = input("Enter your favourite hobby: ")

print(f"Hello {name}! I heard you love {hobby}! That sounds like fun.")

#2
original_price = int(input("Enter original price: "))
discount = int(input("Enter discount percentage (in %): "))

discounted_price = original_price - original_price * discount/100

print("New price: ", discounted_price)


#3
length_m = int(input("Enter length in meters: "))
print(f"Centimeters = {length_m * 100}; Kilometers = {length_m / 1000}")


#4
age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    print("Child")

elif age >= 13 and age <= 19:
    print("Teenager")

elif age >= 20:
    print("Adult")

else: 
    print("Invalid Age.")



#5
is_sunny = True
is_weekend = False
has_plans = True
has_sunglasses = None

has_sunglasses_str = input("Do you have sunglasses? (yes/no): ")

if has_sunglasses_str.lower() == 'yes':
    has_sunglasses = True

elif has_sunglasses_str.lower() == 'no':
    has_sunglasses = False


if (is_sunny and is_weekend and has_sunglasses) or has_plans:
    print("Perfect day for an outing!")

else:
    print("Maybe stay in today.")
