#PART 1 – Basic For Loop Questions

#Q1. Print Numbers
#Use a for loop to print numbers from 1 to 10.

for i in range(1,11,1):
    print(i)

#Q2. Print Even Numbers
Print all even numbers between 1 and 20.

for i in range(1,21,1):
    if(i%2==0):
        print("Even Numbers:",i)


#Q3. Find Sum
#Print the sum of numbers from 1 to 10 using a for loop.
sum=0
for i in range(1,11,1):
    sum=sum+i
print("The sum of numbers from 1to 10:",sum)


#Q4. Multiplication Table
#Take a number from the user and print its multiplication table up to 10.

num=int(input("Enter the number:"))
for i in range(1,11,1):
    multiply=num*i
    print(multiply)

#Q5. Count Characters
#Take a string and count the total number of characters using a for loop.Stop the loop when the number becomes 5.

#PART 2 – Break Related Questions
#Q6. Stop at 5
#Print numbers from 1 to 10.
for i in range(1,11,1):
    print(i)
    if(i==5):
        break


#Q7. Search in List
#Search for number 25 in a list.
#If found, print "Found" and stop the loop.
no=25
for i in range(1,26,1):
    if(i==no):
        print("Found",no)
        break



#Q8. First Negative Number
#Given a list of numbers, print the first negative number and stop the loop.
for i in range(10,-5,-1):
    if(i<0):
        print(i)
        break


#PART 3 – Continue Related Questions
#Q9. Skip 5
#Print numbers from 1 to 10.
#Skip number 5.
for i in range(1,10,1):
    if(i!=5):
        print(i)
        continue
    

#Q10. Skip Even Numbers
#Print numbers from 1 to 20.
#Skip all even numbers.
for i in range(1,21,1):
    if (i%2==0):
       continue
    else:
        print(i)


#Q11. Skip Letter
#Print each character of the string "PYTHON".
#Skip the letter "O".
ch='PYTHON'
length=len(ch)
for i in range(0,6,1):
    if(i==4):
        i=i+1
        print(ch[i])
        break
    else:
        print(ch[i])
        continue

#PART 4 – Pass Related Questions
#Q12. Empty Loop
#Run a loop from 1 to 5 but do nothing inside the loop using pass.

for i in range(1,6,1):
    print(i)
    pass


#Q13. Skip Using Pass
#Loop from 1 to 10.
#If number is 6, just use pass.

for i in range(1,11,1):
    if(i==6):
        pass
    else:
        print(i)

#PART 5 – For-Else Questions
#(Remember: else runs only if the loop is not stopped by break.)


#Q14. Search Number Using for-else
#Search for number 100 in a list.
#If found, print "Found".
#If not found, print "Not Found".

ch=[1,3,90,100,78]
length=len(ch)
for i in range(0,4,1):
    if(ch[i]==100):
        print("This is the found value",ch[i])
        break
    else:
        print("Not Found")
        

#Q15. Prime Number Check
#Take a number from the user and check whether it is prime using for-else.

count=0
num=int(input("Enter the number value:"))
n=int(input("Enter the value of n:"))
for i in range(1,n,1):
        if(num%i==0):
            count=count+1
            if(count>2):
                    print("The number is not a prime number having factors",i)
        
else:
    if(count==2):
        print("The number is a prime number",num)
                

#PART 6 – Pattern Questions
#Q16. Star Pattern
Print:
*
**
***
****
*****


for i in range(1,6):
        for j in range(1,i+1):
          print("*",end='')
        print('')

Q17. Reverse Star Pattern
Print:
*****
****
***
**
*

for i in range(1,6):
        for j in range(6,i,-1):
            print("*",end='')
        print()
            

Q18. Number Pattern
Print:
1
12
123
1234
12345


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()

Q19. Same Number Pattern
Print:
1
22
333
4444
55555

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()


Q20. Pyramid Pattern
Print:
    *
   ***
  *****
 *******
********* 

for i in range(1,10,2):
    for k in range(9,i,-1):
        print(" ",end='')
    for j in range(1,i+1,1):#j<i 1<2,3<4,5<6,7<8
        print("* ",end='')
    print()



Q21. Inverted Pyramid
Print:
*********
 *******
  *****
   ***
    *

k=0
for i in range(9,0,-2):
            print(" "*k,end='')
            k+=1
            for i in range(1,i+1):
                print("*",end='')
            print()
   
Bonus Question
Q22. Break in Pattern
Print a star pattern.
Stop printing when the row number reaches 4.

for i in range(1,10):
    for j in (1,i+1):
        if(i==4):
            break
        else:
            print("*"*i,end='')
    print()

  

