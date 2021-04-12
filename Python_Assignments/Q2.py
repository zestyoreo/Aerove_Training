import math as m

def is_palindrome(n):
    rev=n[::-1]
    if rev==n:
        return True
    else:
        return False

n=int(input("Enter in a palindrome number: "))+1

while not is_palindrome(str(n)):
    n+=1

print(n)