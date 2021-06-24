lis1=["Bengali","Math","English","History","Geography","Life sc.","Phy sc."]
lis2=["Bengali","English","Math","Physics","Chemistry"]

marks=[]
for sub in lis1:
    res=int(input("Enter the 10th result in {} ".format(sub)))
    marks.append(res)
    
    
for i in range(len(marks)-1,0,-1):
    for j in range(i):
        if marks[j]<marks[j+1]:
            temp=marks[j]
            marks[j]=marks[j+1]
            marks[j+1]=temp
    
best=marks[:4]
tenth=sum(best)
tenthp=28*tenth/400

     
total=0
for i in lis2:
        
    eleventh=int(input("Input eleventh number in {} ".format(i)))
    eleventhp=42*eleventh/70
    
    prac=int(input("Enter your practical number "))
    
    totals=int(tenthp+eleventhp+prac)
    print("Your result in {} is {} ".format(i,totals))
    total=int(total+totals)
    
    
print("your total number in Higher secondary is ",total)
avg=total/5

print("You Got {} %".format(avg))

