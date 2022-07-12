#Ask user for name
name=input("What is your name?: ")
print(name)
#Ask user for age
age = input ("What is your age:? ")
print(age)
#Ask user for city
city = input ("What is your city:?")
print(city)
#Ask user what they like doing
love = input ("What do you love to do?")
#Create output text

string = "Your name is {} and you are {} years old.  You live in {} and you love {}"
output = string.format(name, age, city, love)
#Print output to screen
print(output)

