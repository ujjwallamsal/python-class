# Program to check whether the string is Palindrome

def isPalindrome(s):
    return s == s[::-1]
s = "ujjwal"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")
# Program to reverse words in a given String

a = ("ujjwal")
a = a[::-1]
print(a)
# Program to find length of a String
a = "ujjwal"
b = len(a)
print(b)
# Program to count number of vowels in a String
string = (input("Enter string:"))
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)

# Program to split and join a String
a = ["python", "programming"]
string = '-'.join(a)
print(string)

b = "python"
string2 = b.split(" ")
print(string2)
