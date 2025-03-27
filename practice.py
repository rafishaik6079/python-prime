
#1)replace an element
'''s=input("Enter string: ")   #abacd
c1,c2=input("c1,c2: ").split(",")
for i in range(len(s)):
    if s[i]==c1:
        print(s.replace(s[i],c2))
        break'''
#remove element
'''s=input("Enter string: ")   #abacd
c1=input("c1: ")
for i in s:
    if s[i]!=c1:
        print(i,end="")'''

#2)remove space from a list
'''s=input("Enter string: ")
t=""
for i in s:
    if i!=" ":t+=i
print(t)'''

#3)reverse string
'''s=input("Enter string: ").split()
print(s[::-1])

s=input("Enter string: ").split()
for i in range(len(s)-1,-1,-1):
    print(s[i],end=" ")'''

#4)convert string
'''n=input("Enter string: ").split()
for i in n:
    print(i.replace(i[0],chr(ord(i[0])-32)),end=" ")'''

#5)add strings
'''n1,n2=input("Enter two numbers as string: ").split()
n3,n4=input("Enter two numbers as string: ").split()
print(int(n1)+int(n2))
print(int(n3)+int(n4))'''

#6)anagram
'''s=input("Enter a string: ")
t=input("Enter a duplicate string: ")
r=""
for i in s:
    if i in t:
        r+=i
print(r==s)'''

#7)pangram
'''s=input("Enter a string: ")
t="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
u="abcdefghijklmnopqrstuvwxyz"
if len(s)<26 or len(s)>26:
    print("This is not works for pangram.")
else:
    r=""
    for i in s:
        if (i in t) or (i in u):
            r+=i
if s==r:
    print("pangram")
else:
    print("not pangram")'''

#8)string palindrome
'''n=int(input("size: "))
s=input("Enter a string: ")
r=""
if len(s)==n:
    for i in range(len(s)-1,-1,-1):
        r+=s[i]
    print(r==s)
else:print("please enter n number of letters.")'''

#9)all substrings
'''n=input("Enter string: ")
l=0
for l in range(len(n)):
    for i in range(l+1,len(n)+1):
        print(n[l:i])'''



'''l=[1, 10, 3, 11, 6, 15]
n=l[0]
l3=[]
for i in range(1,len(l)):
    if n<l[i]:
        l3.append(n)
print(l3)
l2=[]
s=0
for i in l3:
    s+=i
    l2.append(s)
for i in range(1,len(l)+2):
    if (i not in l) and (i not in l2):
        print(i)
        break'''

#day-3
#rat problem
'''r=int(input("no of rats: "))
u=int(input("unit of food: "))
n=int(input("array size: "))
arr=list(map(int,input("Enter an array: ").split()))
t=r*u
l=len(arr)
s=0
a=0
if len(arr)==n:
    for i in range(0,len(arr),4):
        a=sum(arr[i:(i+(l//2))])
        if i<n-3 and t<=a:
            s=(a-t)
        print(s)'''
#password checker
'''def fun():
    s=input("Enter your password: ")
    if len(s)<4:
        print("password must be 4 or above characters: ")
    else:
        d="1234567890"
        l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        c="abcdefghijklmnopqrstuvwxyz"
        s1=""
        for i in s:
            if (i in d) or (i in l) or (i in c) or (i!=" " and i!="/"):
                s1+=i
        if s1==s and (s1[0] not in d):
            print("password is valid")
        else:
            print("password is not valid")
fun()'''
#1210
#0123
s=input("Enter autobiographical number: ")
l=[int(i) for i in s]
l2=[]
for i in range(len(s)):
    l2.append(l.count(i))
for i in range(len(l2)+1):
    if l2.count(i)==0:
        print(i)
        break

        











