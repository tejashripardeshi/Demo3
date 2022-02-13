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
