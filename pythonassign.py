#1.1 Prime numbers

def primeno(n):
    if (n < 2):
        return False
    else:
        for i in range(2, int(n ** 0.5) +1):
            if (n%2) == 0:
                return False
        return True

def findprime(range1):
    prime = []
    for n in range(2,range1 + 1):
        if primeNo(n):
            prime.append(n)
    return prime

range = 50
result = findprime(range)
print(result)

#1.2 User input table

def printtable(n):
    for i in range(1, 11):
        res = n*i
        print(n," * ", i ," = ", res)

n = int(input("Enter a number"))
print_table(n)

#1.3 Palindrome of String
 
name = input("Enter string")
if (name == name[::-1]):
    print("It is a palindrome")
else:
        print(""It is not a palindrome")

#1.4 String reversal

name= input("Enter the string : ")
print("reverse of the given string is : ", name[::-1])