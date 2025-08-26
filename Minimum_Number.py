'''
Two numbers A and B are passed as input. The program must print the smaller number. 
If both A and B are equal, the print the output as the string value EQUAL.

'''
#Your code below

a=int(input())
b=int(input())
if a<b:
    print(a)
elif a==b:
    print("EQUAL") 
else:
    print(b)