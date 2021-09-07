name=[ 'm', 'a', 'd', 'a', 'm' ]
a=(name[::])
b=(name[-1::-1])
if a==b:
    print("yes! its a palindrome")
else:
    print("no, its not a palindrome")

name=[ 'a', 'b', 'd', 'c', 'e' ]
a=(name[::])
b=(name[-1::-1])
if a==b:
    print("yes! its a palindrome")
else:
    print("no, its not a palindrome")