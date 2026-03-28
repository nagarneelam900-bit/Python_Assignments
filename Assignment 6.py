Python While Loop Exercise
Part 1 – Basic Level
1. Print numbers from 1 to 10 using a while loop.

i=0
while i<=9:

       i+=1
       print(i)

#2. Print even numbers from 1 to 20.
i=0
while i<=20:
    if(i%2==0):
        print(i)
    i+=1


#3. Print odd numbers from 1 to 20.

i=0
while i<=20:
    if(i%2!=0):
        print(i)
    i+=1

#4. Print numbers from 10 to 1 (reverse order).

i=10
while i>0:
    print(i)
    i=i-1

#5. Print multiplication table of 5 using while loop.

i=1
n=5
while i<11:
    multiply=n*i
    print(multiply)
    i+=1


#Part 2 – Intermediate Level
#6. Find the sum of first 10 natural numbers using while loop.

i=1
add=0
while i<11:
    add=add+i
    i=i+1
print("The Sum of first 10 natural numbers is ",add)


#7. Find factorial of a number entered by user.
factorial=1
n=int(input("Enter the no.:"))
while n>0:
    factorial=factorial*n
    n=n-1
print("Factorial of number is:",factorial)


#8. Count number of digits in a given number.
count=0
no=int(input("Enter the number:"))
while no>0:
    rem=no%10
    no=no//10
    count=count+1
print("The count of digits in a given number is:",count)


#9. Reverse a number using while loop.
no=int(input("Enter the number:"))
while(no>0):
    digit=no%10
    reverse=reverse*10+digit
    no=no//10

print("The reverse of number is:",reverse)

#10. Check whether a number is palindrome or not using while loop.

no=int(input("Enter the number:"))
copy=no
reverse=0
while no>0:
        digit=no%10
        reverse=reverse*10+digit
        no=no//10
        
print(reverse)
if(reverse==copy):
        print("True")
        print("Number is a palindrome no",reverse)
else:
        print("False")
        print("Number is not a palindrome no",reverse)



Part 3 – Pattern Based
11. Print pattern:
*
**
***
****
*****

n=int(input("Enter the range value"))
i=1
while i<n+1:
        j=1
        while j<i+1:
            print("*",end='')    
            j=j+1
        print()
        i=i+1

12. Print pattern:
1
12
123
1234
12345

n=int(input("Enter the range value"))
i=1
while i<n+1:
        j=1
        while j<i+1:
            print(j,end='')    
            j=j+1
        print()
        i=i+1


#Part 4 – Logical / Real Scenario
#13. Ask user to enter password until correct password is entered.
password=input("Enter the password:")
passcode='admin1234'
n=input("Enter Chances")
while n<='3':
        if(password==passcode):
                print("Correct Password.Successfully Logged in.")
                break
        else:
                print("Incorrect Password.")
                break
n=n-1

'''
'''
#14. Create a number guessing game:
#• Generate a random number (1–10)
#• Keep asking user until they guess correctly

import random
num=random.randint(1,7)
for i in range(1,4):
    print(i,"chance!")
    u=int(input("Guess a number from 1 to 7:"))
    if num==u:
        print("You guess the right no.")
        print("That was the random no",num)
        break
    else:
        print("You guess Wrong.Try Again")
'''
'''
#15. Keep taking input numbers until user enters 0, then print total sum.
add=0
while True:
    no=int(input("Enter the num:")
      add=add+no

print(add)
          
    

Bonus Challenge (Interview Level)
16. Print Fibonacci series up to N terms using while loop.

a=0
b=1
n=int(input("Enter the value of n:"))
while(n>0):
    c=a+b
    a=b
    b=c
    n=n-1
    print(c)

          

#17. Check whether a number is Armstrong number.
n=int(input("Enter the number:"))
copy=n
add=0
length=len(str(n))
while n>0:
    digit=n%10
    add=add+digit**length
    n=n//10
print(add)
if(copy==add):
    print("Number is an armstrong number:",add)
else:
    print("Number is not an armstrong number:",add)
    


#18. Print prime numbers between 1 to 50 using while loop.

n=int(input("Enter the range:"))
while n>0:
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    
            if count==2:
                print("The prime numbers from 1 to 50 are:",n)
    n=n-1


