#ASSIGNMENT 3-

#A. Python IF (Single Condition)

#1. Write a Python program to check if a number is positive.
num=int(input("Enter the number:"))
if num>0:
    print("Number is positive",num)
else:
    print("Number is negative",num)


#2. Print "Eligible to vote" if age is 18 or above.

age=int(input("Enter the age"))
if age>=18:
    print("Elligible to vote:",age)
else:
    print("Not elligible to vote:",age)


#3. Check if a number is divisible by 7.

num=int(input("Enter the number"))
if(num%7==0):
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")


#4. Print "Pass" if marks are greater than 40.
marks=int(input("Enter the marks:"))
if(marks>40):
    print("PASS",marks)
else:
    print("FAIL",marks)


#5. Check if a number is greater than 100.
num=int(input("Enter the the number:"))
if(num>100):
    print("Number is greater than 100")
else:
    print("Number is smaller than 100")

#6. Display a message if temperature exceeds 45°C.

temp=int(input("Enter the Temperature:"))
if(temp>45):
    print("temperature exceeds 45°C")
else:
    print("Temperature does not exceeds 45°C")

#7. Check if a string length is more than 8 characters.
ch=input("Enter the String")
length=len(ch);
print("The length of String is:",length)
if(length>8):
    print("The length of string is more than 8 characters:",length)
else:
    print("The length of string is less than 8 characters:",length)

#8. Print "Logged In" if password matches "admin123".
password=input("Enter the Password:")
if(password=='admin123'):
    print("Logged In")
else:
    print("Invalid Password")

#9. Check if a number is a multiple of 10.
num=int(input("Enter the number:"))
if num%10==0:
    print("Number is a multiple of 10:",num)
else:
    print("Number is not multiple of 10:",num)

#10. Print a warning if balance is below minimum limit.
balance=float(input("Enter the balance value:"))
minLimit=10000.0
if balance<minLimit:
    print("Warning:Balance is below minimum limit.It Should be:",minLimit)
elif balance>minLimit:
    print("Sufficient Amount.Amount is:",balance)


#B. Python IF–ELSE (Two Conditions)

#11. Check whether a number is even or odd.

num=int(input("Enter the number:"))
if num%2==0:
    print("Even Number:",num)
elif num%2!=0:
    print("Odd Number:",num)

#12. Find the largest of two numbers.

num1=int(input("Enter the number 1:"))
num2=int(input("Enter the number 2:"))
if num1>num2:
    print("num1 is Greater:",num1)
elif num1<num2:
     print("num2 is Greater:",num2)

#13. Check whether a person is eligible for driving license.

MinimumAge=int(input("Enter the age:"))
if MinimumAge>=18:
    print("Person is elligible for driving license",MinimumAge)
elif MinimumAge<=18:
    print("Person is not elligible for driving license",MinimumAge)

#14. Print "Pass" or "Fail" based on marks.

marks=int(input("Enter the marks of student:"))
if marks>=40 and marks<=100:
    print("Pass:",marks)
elif marks>=0 and marks <40:
    print("Fail:",marks)

#15. Check whether a number is positive or negative.
num=int(input("Enter the num:"))
if num>0:
    print("Number is positive:",num)
elif num<0:
    print("number is negative:",num)
else:
    print("Number is zero:",0)

#16. Check whether a character is a vowel or consonant.
ch=input("Enter the character:")
if ch in('A','E','I','O','U'):
    print("Entered Character is vowel:",ch)
elif ch not in('A','E','I','O','U'):
     print("Entered character is consonant:",ch)
else:
    print("Entered character maybe number or special character.",ch)

#17. Check if a year is leap or not.
year=int(input("Enter the year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print("Year is a leap Year",year)
elif (year%4!=0 and year%100==0) or year%400!=0:
    print("year is not a leap Year",year)
else:
    print("Year is:",year)

#18. Print "Valid Password" or "Invalid Password".

password=input("Enter the password:")
passcode='admin1234'
if(password==passcode):
    print("Valid Password.Logged In")
else:
    print("Invalid Password.Please Enter the correct credentials.")

#19. Determine whether salary is taxable or not.
salary=int(input("Enter the salary:"))
minimumSal=800000
if salary<minimumSal:
    print("Salary is not taxable:",salary)
elif salary>minimumSal:
    print("Salary is taxable:",salary)

#20. Check whether a number is greater than 50 or not
num=int(input("Enter the number:"))
if num>50:
    print("Number is greater than 50:",num)
elif num<50:
    print("Number is less than 50:",num)
else:
    print("number is 50:",num)

#C. Python NESTED IF–ELSE

#21. Find the largest of three numbers.
num1=int(input("Enter the value of num1:"))
num2=int(input("Enter the value of num2:"))
num3=int(input("Enter the value of num3:"))
if(num1>num2 and num1>num3):
    print("num1 is greater",num1)
elif(num2>num1 and num2>num3):
    print("num2 is greater",num2)
elif(num3>num1 and num3>num1):
    print("num3 is greater",num3)

#22. Check whether a number is positive, negative, or zero.
#23. Assign grades:
#● A → marks ≥ 90
#● B → marks ≥ 75
#● C → marks ≥ 60
#● Fail → below 60

marks=int(input("Enter the marks of student:"))
if marks>=90 and marks<=100:
    print("Grade A:",marks)
elif marks>=75 and marks<=89:
    print("Grade B:",marks)
elif marks>=60 and marks<=74:
    print("Grade C:",marks)
elif marks<=60:
    print("Fail",marks)
         
#24. Check whether a triangle is equilateral, isosceles, or scalene.

side1=int(input("Enter the side 1 value:"))
side2=int(input("Enter the side 2 value:"))
side3=int(input("Enter the side 3 value:"))
if(side1==side2 and side2==side3 and side3==side1):
    print("Equilateral triangle as all 3 sides are of same value")
elif(side1==side2 and side2!=side3 and side3!=side1):
    print("Isoceles Triangle as two sides are same and one side is of different value")
elif(side1!=side2 and side2!=side3 and side3!=side1):
    print("Scalene Triangle as all the sides are different")

#25. Check whether a character is uppercase, lowercase, digit, or special character.
ch=input("Enter a character:")
ch1=ord(ch)
if ch1>=65 and ch1<=90:
    print("Uppercase Letter:",chr(ch1))
elif ch1>=97 and ch1<=122:
    print("LowerCase letter:",chr(ch1))
elif ch1>=48 and ch1<=90:
    print("Digit:",chr(ch1))
else:
    print("Special Character")
  
#26. Calculate electricity bill using slab-wise rates.
service=250
unit=int(input("Enter unit consumption:"))
if unit<=100:
    bill=unit*5
else:
    if unit<=200:
        bill=unit*7
    else:
        bill=unit*10
bill=bill+service
print("Bill:",bill)

#27. Validate login using username and password.
userName=input("Enter the userName:")
password=input("Enter the password:")
user="PankajNagar"
passcode="admin1234"
if(userName==user and password==passcode):
        print("Valid UserName and password.Logged In")
elif(userName!=user and password!=passcode):
    print("Invalid userName and password.")
elif(userName==user and password!=passcode):
    print("UserName or password is incorrect.")
elif(userName!=user and password==passcode):
    print("Invalid Credentials")
else:
    print("Something Went wrong.")

#28. Check student result using marks of 3 subjects.

marks1=int(input("Enter the marks of subject1:"))
marks2=int(input("Enter the marks of subject2:"))
marks3=int(input("Enter the marks of subject3:"))
Total=marks1+marks2+marks3
print("Total marks of student is:",Total)
if(Total>=60 and Total<=150):
    print("Student passed :",Total)
elif Total<60:
    print("Student Failed:",Total)

#29. Find the second largest number among three numbers.
a=int(input("Enter the First number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if (a>b and a>c):
    if(b>c):
        print("B is second largest number:",b)
    else:
         print("C is second largest number:",c)
elif(b>a and b>c):
    if(a>c):
        print("A is the second largest number:",a)
    else:print("C is second largest number:",c)
else:
    print("A is second largest",a)

   

#30. Check loan eligibility using age, salary, and credit score.
Age= int(input("Enter the age :"))
EmpStatus=input("Enter theEmployment status:")
CreditScore=int(input("Enter the Credit Score:"))
income=float(input("Enter the income value:"))
if(Age>=18 and Age<=70):
         if(EmpStatus=="Salaried" and CreditScore>=750 and income>=25000):
             print("User Eligible for Loan")
         elif(EmpStatus!="Salaried" and CreditScore>=750 and income>=25000):
                 print("User Not eligible for Loan.Not Salaried User")
         elif(EmpStatus=="Salaried" and CreditScore<=750 and income>=25000):
                 print("Credit Score is low.User is not eligible for Loan")
         elif(EmpStatus=="Salaried" and CreditScore>=750 and income<=25000):
                  print("Income below 25000")
         elif(EmpStatus!="Salaried" and CreditScore<=750 and income<25000):
                  print("User not eligible for Loan.Does not meet the criteria.")
else:
    print("User Not eligible for loan.Age is not meeting the criteria")


#D. Python ELIF (Multiple Conditions)
#31. Print day name using day number (1–7).

dayNumber=int(input("Enter the day number:"))
if(dayNumber==1):
    print("Day is Monday")
elif(dayNumber==2):
    print("Day is Tuesday")
elif(dayNumber==3):
    print("Day is Wednesday")
elif(dayNumber==4):
    print("Day is Thursday")
elif(dayNumber==5):
    print("Day is friday")
elif(dayNumber==6):
    print("Day is Saturday")
elif(dayNumber==7):
    print("Day is sunday")
   
#32. Print month name using month number.
monthNumber=int(input("Enter the month number:"))
if(monthNumber==1):
    print("Month is January")
elif(monthNumber==2):
    print("Month is February")
elif(monthNumber==3):
    print("Month is March")
elif(monthNumber==4):
    print("Month is April")
elif(monthNumber==5):
    print("Month is May")
elif(monthNumber==6):
    print("Month is June")
elif(monthNumber==7):
    print("Month is July")
elif(monthNumber==8):
    print("Month is August")
elif(monthNumber==9):
    print("Month is September")
elif(monthNumber==10):
    print("Month is October")
elif(monthNumber==11):
    print("Month is November")
elif(monthNumber==12):
    print("Month is December")

    
#33. Display grade based on percentage.

percentage=int(input("Enter the percentage:"))
if(percentage>80 and percentage<100):
    print("A grade")
elif(percentage<=79 and percentage>=60):
    print("B grade")
elif(percentage<=59 and percentage>=40):
    print("C grade")
elif(percentage<=39 and percentage>=20):
    print("D grade")
else:
    print("F grade.Failed")

#34. Display bonus percentage based on experience years.
bonusper=int(input("Enter the bonus percentage:"))
expYears=int(input("Enter the experience years:"))
if(expYears>=1 and expYears<=3):
     print(f"bonusper is {bonusper}")
elif(expYears>=4 and expYears<=7):
     print(f"bonusper is {bonusper}")
elif(expYears>=8 and expYears<=11):
     print(f"bonusper is {bonusper}")
else:
    print("Less Experience.Not Elligible for bonus.")


#35. Identify traffic signal meaning.
TrafficSignal=input("Enter the Traffic signal colour:")
if TrafficSignal=='Red':
   print("STOP")
elif TrafficSignal=='yellow':
    print("slow down and stop.")
elif TrafficSignal=='green':
    print("GO")


#36. Categorize temperature as Cold / Warm / Hot.
temperature=int(input("Enter the temperature:"))
if(temperature>26):
    print("Hot weather")
elif(temperature==26):
    print("Warm Weather")
elif(temperature<26):
    print("Cold weather")


#37. Categorize employee based on salary range.
salary=int(input("Enter the salary range:"))
if(salary<=4):
    print("Associate Software Engineer")
elif(salary>=5 and salary<=7):
    print("Software Engineer")
elif(salary>=8 and salary<=10):
    print("Senior software Engineer")
elif(salary>=10 and salary<=20):
    print("Lead")
else:print("Manager")

#38. Print discount percentage based on purchase amount.
purchaseAmount=float(input("Enter the purchaseAmount"))
if purchaseAmount>=3000:
     print("Discount is 30%")
if purchaseAmount>=2000 and purchaseAmount<=2999:
    print(f"Discount is 20%")
if purchaseAmount>=1000 and purchaseAmount<=1999:
    print("Discount is 10%")

#39. Identify number type: single-digit / double-digit / multi-digit.

num=int(input("Enter the number:"))
if num>=0 and num<=9:
    print("Single Digit")
elif num<100:
    print("Double Digit")
elif num<1000:
     print("Triple Digit")
else:
    print("Multi Digit")

#40. Assign performance rating: Poor / Average / Good / Excellent
performance=input("Enter the performance value:")
if(performance=='Outstanding')
    print("Excellent. Rating=9")
elif(performance=='Very Satisfactory')
    print("Good. Rating= 8")
elif(performance=='Satisfactory')
    print("Average.Rating=7")
elif(performance=='Unsatisfactory')
    print("Poor.Rating=Below 6")

E. Python COMPLEX CONDITIONS (AND / OR / NOT)

#41. Check whether a number is divisible by 5 and 11.
num=int(input("Enter the number:"))
if(num%5==0 and num%11==0):
        print("Number is divisible by 5 and 11 both:",num)
elif(num%5!=0 and num%11!=0):
        print("Number is not divisible by 5 or 11",num)
else:
    print("Please give correct input")
        

42. Check if a person is eligible for loan:
● age ≥ 21
● salary ≥ 25,000
● credit score ≥ 700

Age= int(input("Enter the age :"))
EmpStatus=input("Enter theEmployment status:")
CreditScore=int(input("Enter the Credit Score:"))
income=float(input("Enter the income value:"))
if(Age>=21 and Age<=70):
         if(EmpStatus=="Salaried" and CreditScore>=700 and income>=25000):
             print("User Eligible for Loan")
         elif(EmpStatus!="Salaried" and CreditScore>=700 and income>=25000):
                 print("User Not eligible for Loan.Not Salaried User")
         elif(EmpStatus=="Salaried" and CreditScore<=700 and income>=25000):
                 print("Credit Score is low.User is not eligible for Loan")
         elif(EmpStatus=="Salaried" and CreditScore>=700 and income<=25000):
                  print("Income below 25000")
         elif(EmpStatus!="Salaried" and CreditScore<=700 and income<25000):
                  print("User not eligible for Loan.Does not meet the criteria.")
else:
    print("User Not eligible for loan.Age is not meeting the criteria")


#43. Validate login using username AND password.
userName=input("Enter the userName:")
password=input("Enter the password:")
user="PankajNagar"
passcode="admin1234"
if(userName==user and password==passcode):
        print("Valid UserName and password.Logged In")
elif(userName!=user and password!=passcode):
    print("Invalid userName and password.")
elif(userName==user and password!=passcode):
    print("UserName or password is incorrect.")
elif(userName!=user and password==passcode):
    print("Invalid Credentials")
else:
    print("Something Went wrong.")

#44. Check student pass condition:
#● All subjects ≥ 40
#● Average ≥ 50

marks1=int(input("Enter the marks of subject1:"))
marks2=int(input("Enter the marks of subject2:"))
marks3=int(input("Enter the marks of subject3:"))
Total=(marks1+marks2+marks3)
Average=Total/3
print("Total marks of student is:",Average)
if(Total>=40 and Average>=50):
    print("Student passed :",Average)
elif Total<40:
    print("Student Failed:",Total)

#45. Check if a number lies between 10 and 100.
num=int(input("Enter the number:"))
if(num>=10 and num<=100):
    print("Number exist between 10 and 100:",num)
elif(num<10 and num>0):
    print("Number is smaller then 10 and belongs to range 0-10")
elif(num>100):
    print("Number is greater than 100")
else:
    print("Enter correct input")

#46. Check exam eligibility:
#● attendance ≥ 75% OR
#● medical certificate available

attendance = int(input("Enter the attendance:"))
medicalCert=input("Enter the value as yes or no:")
if(attendance>=75):
    print("Student elligible for giving exam")
elif attendance<=75 and medicalCert=='Yes':
    print("Student elligible for giving exam")
elif attendance<=75 or medicalCert=='No':
    print("Student not elligible to give exam")

#47. Validate a date using conditions.
day=int(input("Enter Day:"))
month=int(input("Enter Month:"))
year=int(input("Enter Year:"))
if day>0 and day<32 and month>0 and month<13:
    print("Valid Date")
else:
    print("Invalid date")

#48. Check whether an email format is valid.

email=input("Enter an Email Id:"))
if '@' in email and '.' in email:
    print("Valid email:",email)
else:
    print("Invalid Email:",email)

#49. Determine insurance eligibility using age, health status, and income.
age=int(input("Enter the value of Age:"))
healthStatus=input("Enter the value for health status:")
income=int(input("Enter the income:"))
if age>=18 and age<=65:
    if healthStatus=="OK" and (income>=10000 and income<=125000):
        print("Elligible for Insurance")
    elif healthStatus==" NotOK" and (income>=10000 and income<=125000):
        print("Not Elligible for Insurance.")
    elif healthStatus==" OK" and income<=10000:
        print("Not Elligible for Insurance.Income does not match the criteria.")
    elif healthStatus=='OK' and income>=125000:
        print("Elligible for Insurance")
else:
    print("Enter the correct Age.Age does not matched the criteria.")


#50. Check leap year using complete leap year logic.
year= int(input("Enter the year:"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("Year is a leap year")
else:
    print("Year is not a leap year")


#F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS
#51. Write a Python program to calculate income tax using slabs.

income=float(input("Enter the income value:"))
tax=0.0
print("1.Old Tax Regime \n2. New Tax Regime \n 3. Exit")
ch=int(input("enter your choice:"))
if ch==1:
    if(income<250000):
        print("No Tax on income",income)
    elif income>=250000 and income<=500000:
        tax= (income)*0.05
        print(f"The tax value on income {income} is",tax)
    elif income>=500000 and income<=1000000:
        tax= (income)*0.2
        print(f"The tax value on income {income} is",tax)
    elif income>=1000000:
        tax= (income)*0.3
        print(f"The tax value on income {income} is",tax)
elif ch==2:
     if(income<400000):
        print("No Tax on income",income)
    elif income>=400000 and income<=800000:
        tax= (income)*0.05
        print(f"The tax value on income {income} is",tax)
    elif income>=800000 and income<=1200000:
        tax= (income)*0.1
        print(f"The tax value on income {income} is",tax)
    elif income>=1200000 and income<=1600000:
        tax= (income)*0.15
        print(f"The tax value on income {income} is",tax)
    elif income>=1600000 and income<=2000000:
        tax= (income)*0.2
        print(f"The tax value on income {income} is",tax)
    elif income>=2000000 and income<=2400000:
        tax= (income)*0.25
        print(f"The tax value on income {income} is",tax)
    elif income>=2400000:
        tax= (income)*0.3
        print(f"The tax value on income {income} is",tax)
else:
    print("Enter the correct Choice")
        
#52. Create an ATM withdrawal program with balance checks.

bal=900000
print("1.Check Balance\n2.Withdrawal Balance \n 3.Exit")
ch=int(input("Enter Your choice:"))
if ch==1
    print("Your current balance:",bal)
elif ch==2:
    w=int(input("Enter Amount to withdrawal:"))
    if w<=bal:
        print("Balance Withdrawal")
        print("Remaining Amount:",(bal-w))
    else:
        print("Insufficient Balance")
else:
    print("Ok")
    
#53. Check promotion eligibility using experience and performance.
experience=int(input("Enter the years of Experience:"))
PerformanceRating=input("Enter the performance Rating:")
if experience==3 and PerformanceRating=='Satisfactory':
        print("Not Elligible for promotion")
elif experience==3 and PerformanceRating>='Good':
        print("Not Elligible for promotion")
elif experience>=3 and PerformanceRating>='Great':
     print("Elligible for Promotion.")
elif experience>=3 and PerformanceRating>='Outstanding':
    print("Elligible for promotion.")
else:
    print("Poor Performance.Not Elligible for Promotion.")
        

#54. Implement a grading system using nested if–else.
marks=int(input("Enter the marks of student:"))
if marks>=90 and marks<=100:
    print("Grade A:",marks)
elif marks>=75 and marks<=89:
    print("Grade B:",marks)
elif marks>=60 and marks<=74:
    print("Grade C:",marks)
elif marks<=60:
    print("Fail",marks)

#55. Validate strong password using multiple conditions.
userName=input("Enter the userName:")
password=input("Enter the password:")
user="PankajNagar"
passcode="admin1234"
length=len(passcode)
if(length>=8 and '@' in passcode and '0' in passcode and '1' in passcode and 'A' in passcode and 'a' in passcode):
    if(userName==user and password==passcode):
        print("Valid UserName and password. Strong Password.Logged In")
    elif(userName!=user and password!=passcode):
        print("Invalid userName and password.")
    elif(userName==user and password!=passcode):
        print("UserName or password is incorrect.")
    elif(userName!=user and password==passcode):
        print("Invalid Credentials")
else:
    print("Something Went wrong.")

#56. Calculate delivery charges based on location and order amount.

DeliveryCharges=0.0
locDistance =int(input("Enter How Far the Location is:"))
orderAmount=int(input("Enter the order Amount:"))
if order amount >= 400 and orderAmount<=799 and locDistance==10:
    print("Free Delivery.No Charges")
elif order amount >= 800 and orderAmount<=1199 and locDistance==20:
        DelCharges=orderAmount*0.05
        print("Delivery Charge on this order is:",DelCharges)
elif order amount >= 1200 and orderAmount<=1999 and locDistance==30:
        DelCharges=orderAmount*0.05
        print("Delivery Charge on this order is:",DelCharges)
elif order amount >= 1200 and orderAmount<=1999 and locDistance==30:
        DelCharges=orderAmount*0.2
        print("Delivery Charge on this order is:",DelCharges)
else:
    print("We Do not Deliver order in your Area.")
    
#57. Determine online exam qualification.
age=int(input("Enter the Valid age"))
Marks=int(input("enter the Total marks:"))
if Marks>=100 and Marks<=200:
    print("Student Qualified the exam")
elif Marks<100 and Marks>=50:
    print("Student Did not Qualified the exam")
else:
    print("Student Scored in negative ")

#58. Create movie ticket pricing logic based on age & show time.

MovieName=input("Enter the valid movie Name:")
age=int(input("Enter the Valid age:"))
Day=input("Enter the Day for watching Show:")
TicketPrice=500.0
if showTime=='Day' and age>=18 and Day='weekday':
    print("Total ticket Price is:",TicketPrice)
elif showTime=='Day' and age<=18 and age >=10 and Day='weekday':
    price=TicketPrice/2
    print("Total ticket Price is:",price)
elif showTime=='Day' and age<=9 and age >=3 and Day='weekday' :
    price=TicketPrice/4
    print("Total ticket Price is:",price)
elif showTime=='Night' and age>=18 and (Day='Saturday' or Day='Sunday'):
    print("Total ticket Price is:",TicketPrice+100)
elif showTime=='Night' and age<=18 and age >=10 and (Day='Saturday' or Day='Sunday'):
    price=TicketPrice/2 +50
    print("Total ticket Price is:",price)
elif showTime=='Night' and age<=9 and age >=3 and (Day='Saturday' or Day='Sunday'):
    price=TicketPrice/4 +25
    print("Total ticket Price is:",price)
    
#59. Determine bank account type based on balance.
bal=900000
print("1.Check Balance\n2.Withdrawal Balance \n 3.Exit")
ch=int(input("Enter Your choice:"))
if ch==1
    print("Your current balance:",bal)
    if(bal>=10000 and bal<=150000):
        print("Salaried Account")
    elif(bal<10000 and bal>=500):
         print("Savings Account")
    elif(bal>=150000 and bal<=1400000):
        print("Current Account")
elif ch==2:
    w=int(input("Enter Amount to withdrawal:"))
    if w<=bal:
        print("Balance Withdrawal")
        print("Remaining Amount:",(bal-w))
    else:
        print("Insufficient Balance")
else:
    print("Ok")

#60. Create a menu-driven program using if–elif–else

print("1.Starters\n2.Main Course \n 3.Desserts")
NumPeople=int(input("Enter the number of people:"))
price=0.0
Dish=input("Enter the dish:")
beverage='juice'
ch=int(input("Enter Your choice:"))
if ch==1:
    if(dish=='starters' and beverage=="juice")
        price=10.0
        price=price*NumPeople
        print("Order Number is 1. and price is",price)
    elif ch==2:
        if(dish=="Main Course" and beverage=="juice")
            price=500.0
            price=price*NumPeople
            print("Order Number is 2. and price is",price)
    elif ch==3:
        if(dish=="Desserts"and beverage=="juice")
            price=200.0
            print("Order Number is 3. and price is",price)
else:
    print("Dish Not Available.")
