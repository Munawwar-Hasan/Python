# Python Basics – Advanced Practice Set (50 Questions)

#=========================================================================#
# Section 1: Output & Syntax Thinking
#=========================================================================#

# 1. What will the following code print? print('Hello' + 'World')
# -> HelloWorld

#----------------------------------------------------------------#

# 2. Fix the error: print('Hello World)
#--> print('Hello World')

#----------------------------------------------------------------#

# 3. Write a program to print Python is fun using a single print().
# --> print('Python is fun')

#----------------------------------------------------------------#

# 4. What is the output? print('5' * 3)
# --> 555

#----------------------------------------------------------------#

# 5. Difference between print('Hello', 'World') and print('Hello' + 'World')
# --> Print('Hello','World') gives output Hello World that is a space will be printed between Hello and World.
# --> Print('Hello'+'World') gives output HelloWorld that is it will just concatinate the words without any spaces between Hello and World.

#----------------------------------------------------------------#

# 6. Print your name 5 times in one line.
# --> print("John Doe " * 5)

#----------------------------------------------------------------#

# 7. Output of print('Hello\nWorld\nPython')
# --> Hello
# World
# Python

#----------------------------------------------------------------#

# 8. Identify the mistake: print(Hello World)
# --> The error here is abou the quotes missing in the print statement that is ".." or '..' the correct synatx is print("Hello World") OR print('Hello World').

#----------------------------------------------------------------#

# 9. Print Name and Age using escape sequences.
# --> Print("Name : John Doe\nAge : 25")

#----------------------------------------------------------------#

# 10. What happens with print('Hello' * -1)?
# --> Here the output will be an empty string ("") as the multiplication operator is python for strings can post output only id the integer is a positive number(n>0)

#----------------------------------------------------------------#


#=========================================================================#
# Section 2: Variables & Data Types
#=========================================================================#

# 11. Create variables: city, temperature, is_raining.
# --> city = "New York"
# temprature = 30.6
# is_raining = False

#----------------------------------------------------------------#

# 12. Type of x = 10.0?
# --> The type of variable x is float

#----------------------------------------------------------------#

# 13. Output of x='10'; y=5; print(x + str(y))
# --> The output of the given argument is 105

#----------------------------------------------------------------#

# 14. Fix: age='25'; print(age + 5)
# --> print(int(age)+5)

#----------------------------------------------------------------#

# 15. Swap two variables.
# a = 2
# b = 3
# a, b = b, a

#----------------------------------------------------------------#

# 16. Output: a=5; b=a; a=10; print(b)
# -->  5

#----------------------------------------------------------------#

# 17. Can variable start with _? Example.
# --> Yes a variable can start with _ 
# Example : _first_num = 5

#----------------------------------------------------------------#

# 18. Valid names: 1name, name_1, _name, name-1
# --> name_1 and _name

#----------------------------------------------------------------#

# 19. Store birth year and calculate age.
# --> birth_year = int(input("Enter your birth year \t"))
# current_year = 2026
# print("Your age is: ",current_year-birth_year)

#----------------------------------------------------------------#

# 20. Output: x=True; print(type(x))
# --> <class 'bool'>

#----------------------------------------------------------------#


#=========================================================================#
# Section 3: Typecasting Mastery
#=========================================================================#

# 21. Convert '100' to int and multiply by 2.
# --> print(int('100')*2)

#----------------------------------------------------------------#

# 22. What happens: int('abc')?
# --> The program will end up in error as the character values can not be converted to integer.


#----------------------------------------------------------------#

# 23. Convert 5 to string and add ' apples'.
# --> print(str(5),'apples')

#----------------------------------------------------------------#

# 24. Output: print(float(5))
# --> 5.0

#----------------------------------------------------------------#

# 25. Convert '3.14' to float and add 1.
# --> print(float('3.14')+1)

#----------------------------------------------------------------#

# 26. Fix: print(int('10.5'))
# --> print(int(float(10.5)))

#----------------------------------------------------------------#

# 27. Output: print(bool(''))
# --> False

#----------------------------------------------------------------#

# 28. Convert input to int and add 20.
# --> num = (int(input("Enter the number : ")))
# print("Addition of",num,"+ 20 =",num+20)

#----------------------------------------------------------------#

# 29. Output: print(bool('False'))
# --> True

#----------------------------------------------------------------#

# 30. Why does int(True) work?
# --> int(True) works because the boolenas are subclass of integers

#----------------------------------------------------------------#


#=========================================================================#
# Section 4: User Input Logic
#=========================================================================#

# 31. Take name and print Welcome message.
# --> name = input("Enter your name : ")
# print("Welcome", name)

#----------------------------------------------------------------#

# 32. Take age and print next year's age.
# --> age = int(input("Please enter your age : "))
# print ("your age next year will be",age+1)

#----------------------------------------------------------------#

# 33. Take two numbers and print sum.
# --> num_1 = int(input("Enter the first number : "))
# num_2 = int(input("Enter the second number : "))
# print("Addition of ",num_1,"and",num_2,"=",num_1+num_2)

#----------------------------------------------------------------#

# 34. What's wrong: num=input(); print(num+10)
# --> We need to specify that the input is integer by stating it as num=int(input()), because by default python considers the user input as string by default.
# Fix : num=int(input())
# print(num+10)
#----------------------------------------------------------------#

# 35. Take number and print double.
# --> num = int(input("Please enter the number : "))
# print(num*2)

#----------------------------------------------------------------#

# 36. Take input and print type.
# --> input_type = input("Enter any value to find the type of the variable")
# print(type(input_type))

#----------------------------------------------------------------#

# 37. Take first and last name and print full name.
# --> f_name = input("Enter First Name : ")
# l_name = input("Enter Second Name : ")
# print ("Full Name : ",f_name,l_name)

#----------------------------------------------------------------#

# 38. Even or odd check.
# --> num = int(input("Enter a number: "))
# print(["Even", "Odd"][num % 2 != 0])

#----------------------------------------------------------------#

# 39. Square of number using typecasting.
# --> print("Square:", int(input("Number: "))**2)

#----------------------------------------------------------------#


# 40. Print: You entered
# --> print("You entere ", input("Please enter something : "))

#----------------------------------------------------------------#

#=========================================================================#
# Section 5: Operators & Expressions
#=========================================================================#

# 41. Output: print(10/3)
# --> 3.3333333333333335

#----------------------------------------------------------------#

# 42. Output: print(10//3)
# --> 3

#----------------------------------------------------------------#

# 43. Output: print(10%3)
# --> 1 

#----------------------------------------------------------------#

# 44. Area of rectangle.
# --> len = int(input("Please enter the length of the rectangle : "))
# brt = int(input("Please enter the breath of the rectangle : "))
# print("Area of rectangle = ",len*brt)

#----------------------------------------------------------------#

# 45. Simple Interest formula.
# --> Prn_Amt = float(input(("Please enter the Principal Amount : "))
# Int = float(input("Please enter the annual rate of intrest : "))
# Tm = float(input("Please enter the Time period in years"))
# print("So the simple intrest is : " (Prn_Amt*Int*Tm)/100)

#----------------------------------------------------------------#

# 46. Output: print(2**3**2)
# --> 512

#----------------------------------------------------------------#

# 47. Celsius to Fahrenheit.
# --> Cel = float(input("Enter the value in Celsisu : "))
# print(Cel, "in Fahrenheit = " (Cel*9/5)+32)

#----------------------------------------------------------------#

# 48. Output: print(5 + 2 * 3)
# --> 11

#----------------------------------------------------------------#

# 49. Print larger of two numbers.
# --> a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# larger = [a, b][a < b]
# print(f"The larger number is: {larger}")

#----------------------------------------------------------------#

# 50. Average of 3 numbers.
# --> a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# print("Average of",a,b,c,"=",((a+b+c)/3))

#----------------------------------------------------------------#