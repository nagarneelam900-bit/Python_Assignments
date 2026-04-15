String Programming Questions
Basic
1. Write a program to count the number of vowels in a string.

count=0
s="PythonProgramming1"
for x in s:
    if x in ('a','e','i','o','u'):
        print(x)
        count=count+1
print(count)


#2. Reverse a string without using built-in functions.

s="PythonProgramming1"
s1=""
for x in s:
    for i in range(len(s),0,-1):
        s1=s[i-1]
        print(s1,end=' ')
    break


#3. Check whether a string is a palindrome.
s="malayalam"
s1=s
s2=""
for x in s:
    for i in range(len(s),0,-1):
        s2=s[i-1]
        print(s2,end='')
    if(s2==s1):
        print("String is a palindrome")
        break
    else:
        print("String is not palindrome")
        break        

#4. Count uppercase and lowercase letters in a string.
count=0
count1=0
count2=0
s="PythonProgRamming1"
s1=""
for x in s:
    for i in range(0,18):
        if(s[i]>='A' and s[i]<='Z'):
            #print("UpperCase",s[i])
            count=count+1
            
        elif s[i]>='a' and s[i]<='z':
            #print("LowerCase Letter",s[i])
            count1=count1+1
            
        else:
            print("Digit",s[i])
    print("UpperCase letter",count)
    print("Lowercase letter",count1)
    break

5. Replace all spaces in a string with _.

s1="_"
s="Python Programming 1"
"Python Programming 1".replace(" ","_")
print(s)


Intermediate
6. Find the frequency of each character in a string.

s="Python Programming 1"
selected=[]
for x in s:
    for i in range(0,len(s)):
        if s[i] not in selected:
            selected.append(s[i])
            print(f"{s[i]}",s.count(s[i]))
    #print(selected)
    break

#7. Remove duplicate characters from a string.
s="PythonProgramming1"
selected=[]
for x in s:
    for i in range(0,len(s)):
        if s[i] not in selected:
            selected.append(s[i])
    print(selected)
    break

#8. Find the first non-repeating character in a string.
st ="amankumar"
for i in st:
    if st.count(i)==1:
        print(i)
        break
else:
    print("No Non Repeating Character")

9. Check if two strings are anagrams.

st1="SILENT"
st2="LISTEN"
if len(st1)!=len(st2):
    for ch in st1:
        if st1.count(ch)!=st2.count(ch):
            print("Strings are not anagram")
            break
        else:
            print("Strings are Anagram")
else:
    print("Strings are Not Anagram")
10. Convert "hello world" → "Hello World" (title case without using .title()).

s="hello world"
li=list(s)
print(li)
print(len(s))
for x in li:
       for i in range(len(li)):
           if li[i]=='h':
               li[i]='H'
           elif li[i]=='w':
                li[i]='W'
       print(li)
       break

#Tricky

#11. Find the longest word in a sentence.

s="Python programming Language is good "
s1=s.split(" ")
print(s1)
selected=[]
for x in s1:
    for i in range(len(s1)-1):
        #print(s1[i])
        #print(s1[i+1])
        if(len(s1[i])>len(s1[i+1])):
            selected.append(s1[i])
            #s1[i]=s1[i+1]         
    print(selected)
    for j in range(len(selected)-1):
            if(len(selected[j])>len(selected[j+1])):
               print("The longest word is:",selected[j])
            else:
                print("The longest word is:",selected[j+1])
                
    break

12. Compress a string like "aaabbc" → "a3b2c1".
temp=""
st="aaabbc"
count=1
for i in range(0,len(st)):
    if st[i]==st[i+1]:
        count+=1
    else:
        temp=st[i]+str(count)+temp
        count=1
    i=i+1
temp=st[i]+str(count)
print(temp)

13. Count words, characters, and digits in a string.
st="ProgrammingLanguage12"
for i in range(0,len(st)):
    if st[i]>='a' and st[i]<='z':
        count=count+1
        print("character counts:",count)
    elif st[i]>=0 and st[i]<=9:
        count=count+1
        print("Digit counts",count)
    else:
        print("Special Symbol Count:",count)
        
14. Rotate a string left by n positions.
st="AMAN KUMAR"
n=int(input("No. of position by left:"))
for i in range(n):
    st=st[1:]+st[0]
    print(st)
    
15. Find all substrings of a given string.

s = "abc"

# Generate all substrings using list comprehension
substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

# Print the result
print(substrings)
    
Set Programming Questions
Basic


#1. Create a set and add elements dynamically.
s={1}
for i in range(1,10):
    num=int(input("Enter the number"))
    s.add(num)
    print(s)


#2. Find the union and intersection of two sets.

s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
print(s1.union(s2))
print(s1.intersection(s2))


#3. Remove duplicate elements from a list using a set.

li=[2,5,67,78,45,23,67,90]
s=set(li)
print(s)

#4. Check if an element exists in a set.
no=67
s={2,5,67,78,45,23,67,90}
for x in s:
    if no in s:
        print("Exist")
        break
    else:
        print("Don't Exist")

#5. Find the difference between two sets.   
s1={2,5,67,78,45,23,67,90}
s2={45,23,90,21,12,46,78}
print(s1-s2)


#Intermediate
#6. Find common elements in two lists using sets.

li=[2,5,67,78,45,23,67,90]
li1=[45,23,90,21,12,46,78]
s1=set(li)
s2=set(li1)
print(s1.intersection(s2))


#7. Check whether one set is a subset of another.
s={2,5,67}
li=list(s)
s1={{2,5,67},{78,45},{23,67,90}}
li1=list(s1)
print(li1)
for x in li1:
    if li in li1:
        print("Exists",li[x])
    else:
        print("Don't Exists")



#8. Find symmetric difference of two sets.

s1={23,45,67,89,87,56,43}
s2={22,66,43,33,12,86,91,67}
print(s1.symmetric_difference(s2))

#9. Count unique elements in a list using a set.
li=[23,45,67,89,87,56,43,23]
s=set(li)
count=0
for x in s:
    print(x)
    count=count+1
print("The total number of unique elements are",count)

#10. Remove all common elements from two sets.
s1={23,45,67,89,87,56,43}
li=list(s1)
s2={22,66,43,33,12,86,91,67}
li1=list(s2)
li.extend(li1)
print(li)
s3=set(li)
print(s3)

#Tricky
#11. Find missing numbers from 1 to n using sets.
s={1,2,4,5,6,7,8,10}
li=list(s)
n=int(input("Enter the range"))
i=0
selected=[]
diff=li[i+1]-li[i]
for x in li:
    for i in range(len(li)-1):
        if li[i+1]!=li[i]+diff:
            selected.append(li[i]+diff)
            print(selected)
        else:
            print("No Missing Value")
    break


#12. Check if two lists have any common elements.
li=[23,45,67,89,87,56,43]
li1=[22,66,43,33,12,86,91,67]
s=set(li)
s1=set(li1)
print(s.intersection(s1))


#13. Convert a set of strings into uppercase.

s={"Apple","Orange","strawberry"}
s1=str(s)
print(s1.upper())

#14. Identify unique vowels in a given string using a set.
s={"Apple","Orange","strawberry"}
s1=str(s)
print(s1)
li=list(s1)
print("The list is",li)
print(len(li))
unique=[]
for x in li:
    for i in range(len(li)-1):
        #print("The elements in list",li[i])
        if li[i] in ('a','e','i','o','u','A','E','I','O','U'):
                #print("---------",li[i])
                #li[x]=li[x+1]
                unique.append(li[i])
                #print(unique)
                s2=set(unique)
                li[i]=li[i+1]
                break
        else:
           # print("No Unique vowel found")
            li[i]=li[i+1]
print("The set with unique elements",s2)                  

#15. Find elements that appear only once in a list.
li=[23,45,67,89,87,56,43,67,45]
count=0
once=[]
for x in range(len(li)-1):
       # print(f"{li[x]}",li.count(li[x]))
        if li.count(li[x])==1:
            once.append(li[x])
            #print(f"{li[x]} Unique element with count",li.count(li[x]))
print(once)


#Dictionary Programming Questions
#Basic

#1. Create a dictionary and print all keys and values.

s={1:45,2:67,6:89,'A':88}
print(s.keys())
print(s.values())


#2. Count frequency of each word in a sentence.

s="Python Programming is a Good Language to learn and practice"
s1=s.split(" ")
print(s1)
s2=set(s1)
print(s2)
count=0

for x in s2:
    #print(x)
    #count=count+1
    #print(count)
    #print({count:x})


#3. Merge two dictionaries.

s1={1:34,2:67,4:78,'A':54}
s2={6:24,7:90,9:100}
s1.update(s2)
print(s1)


#4. Find the length of a dictionary.
s1={1:34,2:67,4:78,'A':54}
print(len(s1.keys()))


#5. Check if a key exists in a dictionary       
s1={1:34,2:67,4:78,'A':54}
n=4
for k,v in s1.items():
    print(k)
    if(k==n):
        print("Key Exists")
        break
    else:
        print("Key doesnot exists")

#Intermediate
#6. Sort a dictionary by values.
li=[]
s1={1:34,2:89,3:25,5:12,8:90}
for k,v in s1.items():
    li.append(v)
    li.sort()
print(li)

#7. Find the key with the maximum value.
li=[]
s1={1:34,2:89,3:25,5:12,8:90}
for k,v in s1.items():
    t=(k,v)
    #print(t)
    li.append(v)
    li.sort(reverse=True)
    #print(li)
    #print("The maximum value is",li[0])
if li[0] in t:
        print("The key with maximum value is:",k,v)
else:
        print("No")

#8. Remove a key from a dictionary.
s1={1:34,2:89,3:25,5:12,8:90}
s1.pop(3)
print(s1)

#9. Convert two lists into a dictionary.
li=[23,56,78,34,21]
li2=[]
li1=[89,67,33,90,15]
li3=[]
count=0
for x in set(li):
        li2.append((x,count))
        count=count+1
print(li2)
for y in set(li1):
    li3.append((y,count))
    count=count+1
print(li3)
s=dict(li2)
print(s)
s1=dict(li3)
print(s1)
s.update(s1)
print(s)

#10. Count character frequency using a dictionary.
s="Programming"
s1=s.strip("")
print(s1)
li=list(s1)
print(li)
li2=[]
for x in set(li):
        li2.append((x,li.count(x)))
#print(li2)
s2=dict(li2)
print(s2)

#Tricky
#11. Invert a dictionary (swap keys and values).
li=[]
s={1:24,2:65,4:56,8:89,10:67}
for k,v in s.items():
    li.append((v,k))
print(li)
s1=set(li)
print(s1)
s2=dict(s1)
print(s2)


#12. Group elements by frequency using a dictionary.

s={1:12,2:34,3:56,4:67,6:45,7:89,8:12,9:45}
li1=[]
li2=[]
for k,v in s.items():
    li1.append(v)
print(li1)
for x in set(li1):
    li2.append((x,li1.count(x)))
print(li2)
s1=set(li2)
s2=dict(s1)
print(s2)

#13. Find duplicate values in a dictionary.
s={1:12,2:34,3:56,4:67,6:45,7:89,8:12,9:45}
li1=[]
li2=[]
for k,v in s.items():
    li1.append(v)
print(li1)
for x in set(li1):
    li2.append((x,li1.count(x)))
    if(li1.count(x)>1):
        print("Duplicate value:",x)
    else:
        print("No Duplicates")
'''
'''
print(li2)
s1=set(li2)
s2=dict(s1)
print(s2)

#14. Create a nested dictionary for student records.
s={name:Ramesh,Age:12,roll:20}
s1={name:Suresh,Age:23,roll:24}
li=[]
for k,v in s.items():
    li.append((k,v))
print(li)


#15. Flatten a nested dictionary.


#Mixed (String + Set + Dictionary)
#1. Count unique words in a sentence.

s="Programming is Good and it is Good to program"
s1=s.split(" ")
print(s1)
li=list(s1)
li1=[]
for x in li:
    print(f"{x}",li.count(x))
    if x not in li1 and li.count(x)==1 :
        li1.append(x)
        print(li1)
    else:
        print("Duplicate Found")


#2. Find common characters between two strings.

s="Programming is Good"
s1="It is Good to program"
s2=s.split(" ")
s3=s1.split(" ")
s4=set(s2)
print(s4)
s5=set(s3)
print(s5)
s4.intersection(s5)
print(s4)


#3. Find the most frequent character in a string.

s="Proogramming is Good"
s1=s.split(" ")
li=list(s)
li1=[]
for x in set(li):
        print(f"{x}",li.count(x))
        if x not in li1:
            li1.append((x,li.count(x)))
print(li1)
s2=set(li1)
s3=dict(s2)
print(s3)

#4. Remove duplicate words from a sentence.
s="Programming is Good and it is Good to program"
s1=s.split(" ")
s2=set(s1)
print(s2)

#5. Find words with the same letters (anagram groups).
s="silent listen keep peek silet silen"
s1=s.split(" ")
s2=set(s1)
print(s2)
li=list(s2)
li1=[]
for x in set(li): 
    for i in range(len(li)-1):
         if len(li[i])==len(li[i+1]):
            # print(" anagram")
            # print(f"{li[i]}",len(li[i]))
            # print(f"{li[i+1]}",len(li[i+1]))
             li1.append((li[i],li[i+1]))
             li[i]=li[i+1]
             #print(li1)
         else:
             li[i]=li[i+1]
             print("Not Anagram")
print(li1)
             



