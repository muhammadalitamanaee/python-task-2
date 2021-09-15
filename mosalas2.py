print("hello world")
number=int(input("enter max stars you want to display in a line"))
for i in range (1, number+1):
    print(" *" *(i) )
for i in range (number+1 ,0 ,-1):
    print(" *" *i)

