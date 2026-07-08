# You have to take an input of age and tell the person whether they are eligible to vote or not. The voting age is 18 years.

age = int(input("Enter Your Age: ")) 

if age >= 18:
    print("You are eligible for vote.")
else:
    print("You are not eligible for vote.")