
Beginner Level
1. Lambda Basics
o Write a lambda function to add two numbers.

add=lambda a,b:a+b
print(add(10,20))


#o Write a lambda function to check if a number is even or odd.
check_even=lambda num:'even'if num%2==0 else 'odd'
num=int(input("Enter the number:"))
print(check_even(num))


#2. Using map()
#o Given a list of integers, use map() to create a new list with each number squared.
li=[10,20,78,89,56,99]
result=list(map(lambda val:val**2,li))
print(result)

#o Convert a list of strings to uppercase using map().
li=['apple','orange','bottle','pen']
result=list(map(lambda val:val.upper(),li))
print(result)


#3. Using filter()
#o Given a list of numbers, filter out only even numbers.
li=[23,45,67,22,12,13,56,88,10]
li1=[]
check_even=lambda num:li1.append(num) if num%2!=0 else 'odds'
print(list(filter(check_even,li)))

#o Filter words that have length greater than 5 from a list of strings.
li=['apple','orange','bottle','pen','ink']
li1=[]
great_length=lambda words:li1.append(words) if len(words)<=5 else 'smaller'
print(list(filter(great_length,li)))

#4. Using reduce()
#o Find the sum of all elements in a list using reduce().
from functools import reduce
li=[x for x in range(1,11)]
add=lambda a,b:a+b
print(reduce(add,li))

#o Find the product of all numbers in a list.
li=[1,3,4,5,7,8,10]
multiply=lambda a,b:a*b
print(reduce(multiply,li))

#6. Combination of lambda + filter
#o From a list of numbers, filter out all numbers divisible by 3.

li=[10,2,5,7,20,11,33,56,89,36,12,27]
divisible_three=lambda num:num%3==0
print(list(filter(divisible_three,li)))

#7. Using reduce() for maximum
#o Find the maximum number in a list using reduce().
from functools import reduce
li=[23,54,78,89,98,100]
li1=[x for x in li]
result=reduce(lambda num:max(num),li)
print(result)

#8. String Manipulation
#o Given a list of names, use map() to return names with their first letter capitalized.

li=['ramesh','suresh','ram','chandu','lavanya']
result=list(map(lambda name:name.capitalize(),li))
print(result)


#9. Filter Palindromes
#o Given a list of strings, filter out only palindrome words using filter()
def palindrome(li,li1,li2):
    li3=[]
    li4=[]
    for x in range(len(li1)-1,-1,-1):
        li3.append(li1[x])
        print(li3)
    if li2==li3:
        print("Palindrome")
    else:
        print("Not Palindrome")
li=['malayalam','ramesh','suresh','pass','saas']                 
for x in li:
    print(x)
    li1=list(x)
    print(li1)
    #li=list(s)
    li2=li1
    print(li2)
    palindrome(li,li1,li2)



