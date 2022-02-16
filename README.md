# Demo3
write a program to check if the given number is happy number or print all the happy number between 1 to 100
STEP 1:isHappyNumber() determines whether a given number is happy or not.
If the number is greater than 0, then calculate the remainder rem by dividing the number with 10.
Calculate the square of rem and add it to a variable sum.
Divide number by 10.
Repeat the steps from a to c till the sum of the square of all digits present in number has been calculated.
Finally, return the sum.
STEP 2:Define and initialize variable num.
STEP 3:Define a variable result and initialize it with a value of num.
STEP 4:If the result is neither equal to 1 nor 4 then, make a call to isHappyNumber().
STEP 5:Otherwise, if the result is equal to 1 then, the given number is a happy number.
STEP 6:If the result is equal to 4 then, the given number is not a happy number.

# OOP's Concepts
1. Encapsulation : Encapsulation in Python is the process of wrapping up variables andmethods into a single 
entity. In programming, a class is an example that wraps all the variables and methods defined inside it.
Encapsulate means to hide. Encapsulation is also called data hiding
2. Inheritance: In inheritance, the child class acquires the properties and can access all the data members and functions defined in the 
parent class. A child class can also provide its specific implementation to the functions of the parent class.
The idea of reusability is called the inheritance
3. Polymorphism: It is a word that came from two greek words, poly means many and morphos means forms. If a variable, object or method perform different behavior according to situation, it is called polymorphism.
