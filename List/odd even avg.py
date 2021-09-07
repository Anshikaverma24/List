elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
while index<len(elements):
    if elements[index]%2!=0:
        print("odd numbers:", elements[index])
    elif elements[index]%2==0:
        print("even numbers:", elements [index])
    index+=1