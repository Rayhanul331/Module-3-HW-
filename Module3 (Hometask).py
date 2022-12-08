'''
Question 01: Write a program that switches the values stored in the variables a and b. Your program should work for
different inputs. e.g. any value of a and b
'''
a = input("a: ")
b = input("b: ")

x = b
b = a
a = x

print("a: " + a)
print("b: " + b)
'''
Question 02: There are errors in all of the lines of code. Fix the code so that it runs without errors. The output in your 
program should match the example output shown below exactly, character for character, even spaces and symbols should be 
identical, otherwise, the tests won't pass. 

When you run your program, it should print the following:
#Your Output should be exactly like the below 👇

Day 1 - String Manipulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + "world")
New lines can be created with a backslash and n.
#Your Output should be exactly like the above 👆
'''
print("Day",1,"-", "String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print("e.g. print(\"Hello \"", "+","\"world\")")
print("New lines can be created with a backslash and n.")
'''
Question 03: Kitty sent a message with EID Mubarak to her 40 friends on Facebook. Half of them did not even do seen the message.
Of the seen messages, half of them again forwarded the message to 10 of their friends. How many people got the EID Mubarak 
message, keep your answer in the variable named MSG_got.
'''
sent_msg = 40
seen_msg = sent_msg//2
msg_fwd = (seen_msg//2)*10
MSG_got = sent_msg + msg_fwd
print(MSG_got)
'''
Question 04: What will be the value of a? 
2 + 3 + 5 + 8 + 13 + a
use maximum 2 variables to solve this. Keep the answer in variable a. 
'''
b = 13+8
a = b
print("a:", a)
'''
Question 05: Write a code that can give you a total or summation from a to b.
Suppose,
a = 10
b = 90
Keep the answer in the variable named SUM
Hint: use formula for the following 10+11+12+…….+88+89+90 = ?
'''
a = 10
b = 90
x = (b*(b+1))/2
y = (a*(a+1))/2
SUM = x-y
print(int(SUM))


