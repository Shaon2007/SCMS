###################################CLASS 10 HALF YEARLY PROGRAMS################################
# BUZZ NUMBER
n = int(input("Enter the number:"))
if n%7==0 or n%10==7:
	print("The number is buzz")
else:
	print("The number is not buzz")


# ODD NUMBERS
n = int(input("Enter first number:"))
m = int(input("Enter second number:"))
print("Odd numbers between", n, "and", m, "are: ")
for i in range(n, m + 1):
	if i%2!=0:
		print(i, end=", ")


# PRIME NUMBER
n = int(input("Enter the number:"))
for i in range(2, n):
	if n%i==0:
		print("The number is not prime")
		break
else:
	print("The number is prime")


# DUCK NUMBER
n = int(input("Enter the number:"))
for i in str(n):
	if i=="0":
		print("The number is duck")
		break
else:
	print("The number is not duck")


# ARMSTRONG NUMBER
n = input("Enter a number:")
s = 0
for i in n:
	s += int(i) ** 3
if s==int(n):
	print("The number is armstrong")
else:
	print("The number is not armstrong")


# SUM OF DIGITS
n = input("Enter the number: ")
s = 0
for i in n:
	s += int(i)
print("The sum of the digits is:", s)


# NIVEN NUMBER
n = int(input("Enter the number:"))
s = 0
for i in str(n*n):
	s += int(i)
if s == n:
	print("The number is a niven number")
else:
	print("The number is not a niven number")


# FACTORIAL
n = int(input("Enter a number:"))
f = 1
for i in range(n, 1, -1):
	f *= i
print(n, "! is ", f)


# EVEN DIGITS
n = input("Enter a number:")
print("The even digits are:")
for i in n:
	if int(i)%2==0:
		print(i, end=", ")


# SUM OF EVEN DIGITS
n = input("Enter a number:")
s = 0
for i in n:
	if int(i)%2==0:
		s += int(i)
print("The sum of even digits is", s)


# SEIRES 1 4 7 10 ... 97 100
for i in range(1, 101, 3):
	print(i, end=", ")


# SERIES: 1 4 9 16 ... 81 100
for i in range(1, 11):
	print(i**2, end=", ")


# PALINDROME
n = int(input("Enter a number:"))
r = ""
for i in str(n):
	r = i + r
if n == int(r):
	print("The number is palindrome")
else:
	print("The number is not palindrome")


# PAL-PRIME
n = int(input("Enter a number:"))
r = ""
for i in str(n):
	r = i + r
for i in range(2, n):
	if n%i==0:
		print("The number is not pal-prime")
		break
else:
	if n==int(r):
		print("The number is pal-prime")
	else:
		print("The number is not pal-prime")


# LENGHT OF STRING
s = input("Enter a string:")
print("The string is", len(s), "characters long")


# NUMBER OF VOWELS
s = input("Enter a string:")
c = 0
for i in s:
	if i  in "AEIOUaeiou":
		c += 1
print("Number of vowels:", c)


# NUMBER OF CAPITAL LETTERS
s = input("Enter a string:")
c = 0
for i in s:
	if i.isupper():
		c += 1
print("Number of Capital Letters:", c)


# NUMBER OF WORDS
s = input("Enter a string:")
c = 0
for i in s.split(" "):
	if i!="":
		c+=1
print("Number of words:", c)


# VERB REPLACEMENT
s = input("Enter a string:")
print("Modified string:", s.replace(" is ", " was "))


# REVERSE STRING
s = input("Enter a string: ")
r = ""
for i in s:
	r = i + r
print("The reversed string:", r)


# LONGEST WORD
w = ""
for i in input("Enter a string:").split(" "):
	if len(i)>len(w):
		w = i
print("Longest word:", w)


# SUM OF 10 NUMBERS
s = 0
print("Enter 10 numbers:")
for i in range(10):
	s += float(input())
print("Sum:", s)


# MAX, MIN, AVG OF 10 NUMBERS
l = []
print("Enter 10 numbers:")
for i in range(10):
	l.append(float(input()))
print("Maximum:", max(l), "Minimum:", min(l), "Average:", sum(l)/10)


# REVERSE 10 NUMBERS
l = []
print("Enter 10 numbers:")
for i in range(10):
	l.append(input())
print("Numbers in reversed order:")
for i in range(9, -1, -1):
	print(l[i])


# FIRST, LAST AND MIDDLE EMELEMT
l = []
n = int(input("Enter the number of elements:"))
print("Enter", n, "element(s)")
for i in range(n):
	l.append(input())
print("First Element:", l[0], "Last Element:", l[-1], "Middle Element:", l[n//2])


# SUM OF EVEN NUMBERS OF GIVEN NUMBER OF NUMBERS
n = int(input("Enter the number of elements:"))
s = 0
print("Enter", n, "element(s)")
for i in range(n):
	x = int(input())
	if x%2==0:
		s += x
print("Sum of even numbers:", s)


# SUM OF MULTIPLES OF 7 AMONG 10 NUMBERS
s = 0
print("Enter 10 numbers:")
for i in range(10):
	n = int(input())
	if n%7==0:
		s += n
print("Required sum:", s)


# AVERAGE OF 10 NUMBERS
l = []
print("Enter 10 numbers:")
for i in range(10):
	l.append(float(input()))
print("Average of the given numbers:", sum(l)/10)


# BUZZ NUMBERS FROM GIVEN NUMBERS
l = []
n = int(input("Enter the number of numbers"))
print("Enter", n, "numbers:")
for i in range(n):
	x = int(input())
	if x%7==0 or x//10==7:
		l.append(x)
print("Buzz numbers:")
for i in l:
	print(i, end=", ")

