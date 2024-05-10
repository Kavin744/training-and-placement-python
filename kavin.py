1.Write a program to create a new string made of an input string’s first, middle, and last character. Eg: str1= ”PRADEEP” Output: PDP

str=input("Enter a string:")
a=len(str)//2
print(str[0]+str[a]+str[-1])
     
Enter a string:PRADEEP
PDP

2.Write a program to create a new string made of the middle three characters of an input string. Eg: str1= “PRADEEP”
Output: ADE

str=input("Enter a string:")
a=len(str)//2
b=a-1
c=a+1
print(str[b]+str[a]+str[c])

     
Enter a string:PRADEEP
ADE

3.Given two strings, str1 and str2. Write a program to create a new string str3 by appending str2 in the middle of str1. Eg: str1= ”STAR” str2= “SUPER” Output: STSUPERAR

a=input("Enter a string:\n")
b=input("Enter a string:\n")
d=len(a)//2
c=a[0:d]
e=a[d:len(a)]
print(c+b+e)

     
Enter a string:
STAR
Enter a string:
SUPER
STSUPERAR

4.Given two strings, str1 and str2, write a program to return a new string made of str1 and str2’s first, middle, and last characters. Eg: str1= “LEO” str2= “DAS” Output: LDEAOS

a=input("Enter a string:\n")
b=input("Enter a string:\n")
for i in range(len(a)):
    c=a[i]+b[i]
    print(c,end="")

     
Enter a string:
LEO
Enter a string:
DAS
LDEAOS

5.Given two strings, str1 and str2, write a program to return a new string made of str1 and str2’s in reverse order. Eg: str1= ”SUPER” str2= ”STAR” Output: RATSREPUS

a=input("Enter a string:\n")
b=input("Enter a string:\n")
c=a[::-1]
d=b[::-1]
print(d+c)
     
Enter a string:
SUPER
Enter a string:
STAR
RATSREPUS

6.Count all letters, digits, and special symbols from a given string str1 = "P@#yn26at^&i5ve" Outcome: Total counts of chars, digits, and symbols Chars = 8 Digits = 3 Symbol = 4

a=input("Enter a string:\n")
charcount=0
digitcount=0
symbolcount=0
for i in a:
    if i.isalpha():
        charcount+=1
    elif i.isalnum():
        digitcount+=1
    else:
        symbolcount+=1
print(charcount)
print(digitcount)
print(symbolcount)


     
Enter a string:
P@#yn26at^&i5ve
8
3
4

7.Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result. s1 = "Abc" s2 = "Xyz" Output: AzbycX

a=input("Enter a string: \n")
b=input("Enter a string: \n")
c=b[::-1]
for i in range(len(a)):
    d=a[i]+c[i]
    print(d,end="")

     
Enter a string: 
Abc
Enter a string: 
Xyz
AzbycX

8.Write a program to calculate Employee’s bonus calculation for the details given below Experience Bonus (%) More than 8 years 10 % More than 4 years 7% More than 2 years 4%

n=int(input("Enter no of years:\n"))
a=int(input("Enter salary:\n"))
b=a*(10/100)
c=a*(7/100)
d=a*(4/100)
if(n>8):
    print("10% bonus is:",b)
elif(n>4):
    print("7% bonus is:",c)
elif(n>2):
    print("4% bonus is:",d)
else:
    print("Invalid")
     
Enter no of years:
9
Enter salary:
12000
10% bonus is: 1200.0

9.Write a program to calculate the electricity bill (accept number of units from user) according to the following criteria:
Units Price First 100 units No charge Next 100 units Rs.5 per unit After 200 units Rs.10 per unit (For example, if input unit is 350, then the total bill amount is Rs.2000)


n=int(input("Enter no of units:\n"))
if(n<100):
    print("No charge")
else:
    if(n>=100 and n<200):
        print(f"The charge for{n} units is:",((n-100)*5))
    elif(n>=200):
        print(f"The charge for {n} units is:",((n-200)*10)+500)
    else:
        print("not valid")
     
Enter no of units:
350
The charge for 350 units is: 2000

10.Accept the marked price from the user and calculate the Net amount as (Marked Price - Discount) to pay according to following criteria: Marked Price Discount
10000 20%

7000 and <=10000 15%

<=7000 10%


a=int(input("Enter Marked amount:\n"))
if(a>10000):
    b=(a-(a*(20/100)))
    print("The Netamount is:",b)
elif(a>7000 and a<=10000):
    c=(a-(a*(15/100)))
    print("The Netamount is:",c)
elif(a<=7000):
    d=(a-(a*(10/100)))
    print("The Netamount is:",d)
else:
    print("Enter valid input")
     
Enter Marked amount:
12000
The Netamount is: 9600.0

11.Write a program to find the given number is prime number or not.

num=int(input("Enter a number:\n"))
a = False
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            a = True
            break
    if a:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

Enter a number:
11
11 is a prime number

12.Write a program to display all prime numbers within a range

a= int(input ("Enter starting value: "))
b= int(input ("Enter last Value: "))

print ("The Prime Numbers in the range are: ")
for i in range (a,b+1):
    if i > 1:
        for j in range (2,i):
            if (i%j) == 0:
                break
        else:
            print (i)
     
Enter starting value: 10
Enter last Value: 30
The Prime Numbers in the range are: 
11
13
17
19
23
29

13.Write a program to reverse a number? Example: 3256 will be printed as 6523 (reverse order)

a=int(input())
sum=0
while(a!=0):
    sum=sum*10+(a%10)
    a//=10
print(sum)

     
3256
6523

14.Write a program to print the following pattern *
* * *
* * * * *
* * * * * * *

for i in range(5):
    for j in range(4-i):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for x in range(i):
        print("*",end=" ")
    for n in range(4-i):
        print(" ",end=" ")
    print()
     
        *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * *

15.Write a program to print the Fibonacci Series up to 10 terms.

n=int(input("Enter a:\n"))
a=0
b=1
if n<=1:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(3,n+1):
        res=a+b
        a=b
        b=res
        print(res)

Enter a:
10
0
1
1
2
3
5
8
13
21
34
