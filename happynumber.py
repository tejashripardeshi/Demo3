#write a program to check if the given number is happy number or print all the
#happy number between 1 to 100

#is HappyNumber() will determine wether a number is happy or not
def isHappyNumber(num):
    rem = sum = 0

#calculates the sum of squares of digits
    while(num>0):
        rem = num%10
        sum = sum + (rem*rem)
        num = num//10
    return sum
##num = 82
##result = num

#Dusplays all happy numbers between 1 and 100
print("List of happy number between 1 and 100:")
for i in range(1, 101):
    result = i

#happy number always ends with 1
#Unhappy number ends in a cycle of repeating numbers which contain 4
    while(result != 1 and result != 4):
        result = isHappyNumber(result)
    
##if(result == 1):
##    print(str(num)+"is a happy number")

##elif(result == 4):
##    print(str(num)+"is not a happy number")

    if(result == 1):
        print(i)
        print(" ")

