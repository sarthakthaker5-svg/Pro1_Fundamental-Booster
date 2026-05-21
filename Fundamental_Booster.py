print("Welcome to the Interactive Personal Data Collector!")

name=input("Please Enter your name:")
age=int(input("Please Enter your age:"))
height=float(input("Please Enter your height in meters:"))
number=int(input("Please Enter your favorite number:"))

birth_year=2026-age
print("THANK YOU! Here is the information we collected:")

print(f"Name: {name} | Type: {type(name)} | Memory Address: {id(name)}")
print(f"Age: {age} | Type: {type(age)} | Memory Address: {id(age)}")
print(f"Height: {height} | Type: {type(height)} | Memory Address: {id(height)}")
print(f"Favorite Number: {number} | Type: {type(number)} | Memory Address: {id(number)}")

print(f"\nYour Birth Year is approximately: {birth_year}")

print("Thank You for using the Personal Data Collector. GoodBye!")