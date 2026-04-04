#Python Programming Questions – LIST
#Basic Level
#1. Write a Python program to create a list of integers and print its elements.
li=[10,20,30,78,97]
print(li)

#2. Write a program to find the sum and average of all elements in a list.
li=[34,56,89,86,99]
print("The sum of elements in list is:",sum(li))
print("The average of elements in list is:",sum(li)/len(li))

#3. Write a program to find the largest and smallest element in a list.
li=[64,99,890,76,56,23,12,3]
print("The largest element in list:",max(li))
print("The smallest element in list is:",min(li))

#4. Write a Python program to count the number of elements in a list without using len().
li=[89,56,4,3,57,80,39]
count=0
print(li)
for x in li:
    count=count+1
print(count)


#5. Write a program to reverse a list without using built-in functions.
li=[97,96,95,64,79,23,48,12,34]
print(li)
for x in li:
    for i in range(8,-1,-1):
        print (li[i])

#6. Write a program to check if an element exists in a list.
li=[67,34,45,23.4,'abcd']
for x in li:
        if (x=='abcd'):
            print("found",x)
        else:
            print("Not Found",x)

#7. Write a Python program to remove duplicate elements from a list.
li=[97,96,95,64,79,23,48,12,34,97,23]
li_set=set(li)
print(li_set)

#8. Write a program to sort a list in ascending and descending order.
li=[97,96,95,64,79,23,48,12,34,97,23]
li.sort()
print(li)
li.sort(reverse=True)
print(li)

#Intermediate Level
#9. Write a program to merge two lists and remove duplicates.

li=[23,54,34,23,12]
li1=[21,10,90,87,99,98]
li2=li+li1
print(li2)
li3=set(li2)
print(li3)
li4=list(li3)
print(li4)


#10. Write a program to find common elements between two lists.
li=[23,54,34,23,12]
li1=[21,10,90,87,99,98,34,12]
li2=[x for x in li if x in li1]
print(li2)


#11. Write a program to split a list into even and odd numbers.
li=[21,10,90,87,99,98,34,12]
li1=[x for x in li if x%2==0]
li2=[x for x in li if x%2!=0]
print(li1)
print(li2)


#12. Write a program to rotate a list by n positions.
li=[1,2,3,4,5,6,7,8,9,10]
print(li)
n=int(input("No of Right Rotation:"))
for i in range(n):
    val=li.pop(len(li)-1)
    li.insert(0,val)
print(li)

#13. Write a Python program to find the second largest number in a list.
li=[21,10,90,87,99,98,34,12]
li.sort(reverse=True)
print("The second largest number in list is:",li[1:2])


#14. Write a program to flatten a nested list.
li=[[12,34,67],[5,6,89],[45,78,67]]
f_li=[]
print("Nested list",li)
for i in x:
    f_li.append(i)
print("Flatten list:",f_li)

#15. Write a program to count frequency of each element in a list.
count=0
li=[21,10,90,87,99,98,34,12,34,90,90]
li.sort(reverse=True)
print(li)
t=tuple(li)
print(t)
for i in t:
   print(f"The frequency of each element is {i}",t.count(i))

#16. Write a program to replace all negative numbers with zero in a list.
li1=[21,-10,90,87,99,98,34,-12,34,-90,90]
li2=[x for x in li1 if x<0 ]
li3=[x*0 for x in li1 if x<0 ]
print(li2)
print(li3)

Or

given_list = [1, 2, 3, 4, -1, -4, 5, -6]

print(f'List before changes: {given_list}')

for i in range(len(given_list)):
    if given_list[i] < 0:
        given_list[i] = 0

print(f'List after changes: {given_list}')


#Advanced Level
#17. Write a program to remove all occurrences of a given element from a list.
n=int(input("Enter the number:"))
li=[34,67,43,21,12,78,98,90,21]
for i in li:
    if n in li:
      li.remove(n)
print(li)


#18. Write a program to check if a list is a palindrome.

a = [1, 2, 3, 2, 1]
is_palindrome = all(a[i] == a[-(i+1)] for i in range(len(a) // 2))
print(is_palindrome)
   
#19. Write a Python program to find missing numbers in a given list of consecutive integers.

li=[1,2,3,5,6,7,8,10]
diff=li[1]-li[0]
flag=0
for i in range(0,len(li)-1):
    if li[i]+diff!=li[i+1]:
        print(f"{i+2} place missing value:",li[i]+diff)
        flag=1
    if flag==1:
        print("No missing value")
        
#20. Write a program to perform element-wise addition of two lists.

li=[34,67,89,23,78,'abcd']
li1=[67,88,99,12,56,'54']
for x in range(len(li)):
    for i in range(len(li1)):
        li2=li[x]+li1[x]
        print (li2)
        break

#21. Write a Python program to find the longest increasing subsequence in a list.
li=[21,78,89,765,23,23,35,39,45,667,8,9,635,58]
longest_sub_seq=[]
temp=[]
for i in range(0,len(li)-1):
    if(li[i]<li[i+1]:
       temp.append(li[i])
    else:
        temp.append(li[i])
        if(len(temp)>len(longest_sub_seq):
           longest_sub_seq=temp
           temp=[]
print(longest_sub_seq)


#22. Write a program to group elements based on frequency
count1=0
li=[78,98,99,100,98,98,75,98]
li1=[]
for x in range(len(li)):
        count1=li.count(li[x])
       # print(f"{li[x]}",(count1))
        li1.insert(li[x],count1)
        li.insert(li[x],count1)
        li2=[(li[x],li1[x])]
        print(li2)        

#Python Programming Questions – TUPLE
#Basic Level

#23. Write a Python program to create a tuple and print its elements.

t=(23,45,67,78,9,10)
print(t)

#24. Write a program to find the length of a tuple.

t=(23,45,67,78,9,10)
print(len(t))


#25. Write a program to find the maximum and minimum element in a tuple.

t=(23,45,67,78,9,10)
print(max(t))
print(min(t))


#26. Write a program to convert a tuple into a list.
t=(34,78,98,99,100,67,75,72)
li=list(t)
print(li)


#27. Write a program to check if an element exists in a tuple.
t=(34,78,98,99,100,67,75,72)
a=98
for x in range(len(t)):
    if t[x]==98:
        print("Found")
    else:
        print("Not Found")


#28. Write a program to count occurrences of an element in a tuple
count=0
t=(34,78,98,99,100,98,67,98,75,72)
a=98
for x in range(len(t)):
    if t[x]==98:
        print("Found")
        count=count+1
print(count)

#Intermediate Level

#29. Write a program to slice a tuple and display the result.

t=(34,78,98,99,100,98,67,98,75,72)
print(t)
print(t[2:6])

#30. Write a program to find repeated elements in a tuple.
count=0
t=(34,78,98,99,100,98,67,98,75,72,78)
for x in range(len(t)):
      if(t.count(t[x]))>1:
          print (t[x])
    

#31. Write a program to merge two tuples.
t=(34,78,98,99,100,98,67,98,75,72)

t2=(67,88,12,'abcd',87,10)
t3=t+t2
print(t3)

#32. Write a program to unpack elements of a tuple into variables.
ch='a'
ch1='z'
t=(34,78,98,99,100,98,67,98,75,72)
for x in range(len(t)):
    for ch in range(chr('a'),chr('j')):
        print(chr('a'),t[x])
        ch=ch+1


#33. Write a Python program to sort a tuple.
t=(34,78,98,99,100,98,67,98,75,72)
li=list(t)
print(li)
li.sort()
print(li)

#34. Write a program to convert a list of tuples into a dictionary.

t=(34,56,67,89)
s=set(t)
for x in s:
      for i in range(1,4):
               print({i:x})
#Advanced Level
#35. Write a program to find the index of an element in a tuple.
t=(34,78,98,99,100,98,67,98,75,72)
for x in range(len(t)):
    print(t.index(t[x]),"index of ",t[x])


#36. Write a program to remove an element from a tuple (without directly modifying it).

t=(34,78,98,99,100,98,67,98,75,72)
li=list(t)
print(t)
li.remove(100)
print(li)
t1=tuple(li)
print("The modified tuple is:",t1)
print("The original tuple is:",t)
   


#37. Write a program to find common elements between two tuples.

t=(34,78,98,99,100,98,67,98,75,72)
li=list(t)
t1=(34,21,22,86,98,99,10,32)
li1=list(t1)
li2=[x for x in li if x in li1]
print(li2)        


#38. Write a Python program to check if a tuple is a palindrome.
a = (1, 2, 3, 2, 1)
li=list(a)
is_palindrome = all(li[i] == li[-(i+1)] for i in range(len(li) // 2))
print(is_palindrome)

#39. Write a program to find the element with maximum frequency in a tuple.
count1=0
t=(34,78,98,99,100,98,67,98,75,98,72)
li=list(t)
li1=[]
for x in range(len(li)):
    count1=li.count(li[x])
    print(f"{li[x]}",(count1))


#40. Write a program to create a nested tuple and access its elements.
t=((34,78,98,99,100),(98,67,98,75,98,72))
for x in range(len(t)):
    for i in range(len(t[x])):
        print(t[x][i])






