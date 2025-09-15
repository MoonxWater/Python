# num = int(input("Enter a number: "))

# if num % 2: print("Odd")

# else: print("Even")


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


#Create variables: gpa (float, e.g., 3.8), extracurriculars (integer, e.g., 3), is_eligible_for_financial_aid (Boolean, e.g., True). 
#Use nested if statements to check for scholarship eligibility:
# First, check if gpa is 3.5 or higher.
# Inside that if block, check if extracurriculars is 2 or more.
# Inside that if block, check if is_eligible_for_financial_aid is True.
# If all conditions are met, print "Eligible for full scholarship!".
# Provide else statements for each level of nesting to explain why the student is not eligible (e.g., "GPA too low", "Not enough extracurriculars", "Not eligible for financial aid").

gpa = 3.9
extracurriculars = 4
is_eligible_for_financial_aid = True

if gpa >= 3.5:
    if extracurriculars >= 2:
        if is_eligible_for_financial_aid:
            print("Eligible for full scholarship!")
        
        else:
            print("Not eligible for financial aid")
    
    else:
        print("Not enough extracurriculars")

else:
    print("GPA too low")