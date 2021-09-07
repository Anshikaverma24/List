elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
length= len(elements)
index=0
odd_numbers=0
even_numbers=0
while index<length:
    if elements[index]%2!=0:
        odd_numbers=odd_numbers+1
    elif elements[index]%2==0:
        even_numbers=even_numbers+1
    index+=1
print("ODD NUMBER : ", str(odd_numbers))
print("EVEN NUMBER : ", str(even_numbers))
