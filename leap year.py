n1=int(input("enter the start year:"))
n2=int(input("enter the end year:"))
print("the leap year between",n1,"and",n2,"are:")
for i in range(n1,n2):
    if(i%4==0 and i%100!=0 or i%400==0):
        print(i)