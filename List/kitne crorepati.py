amount = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
index=0
crorepati=0
lakhpati=0
dilwale=0
length= len(amount)
while index<length:
 if amount[index]<=10000000:
    crorepati= crorepati+1
 elif amount[index]>=100000 :
    lakhpati= lakhpati+1
 elif amount[index]>=10000:
    dilwale=dilwale+1
 index+=1
print("crorepati : ", str(crorepati))
print("lakhpati : ", str(lakhpati))
print("dilwale : ", str(dilwale))
