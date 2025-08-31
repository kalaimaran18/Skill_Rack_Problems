# Sum_Of_Even

num=int(input())
count=0
for i in range(1,num):
    if i%2==0:
        count=count+i
print(count)

#ex:output
#input(1,11)  sum(2,4,6,8,10)
#output(30)