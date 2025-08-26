'''
A single character C is passed as the input to the program. 
Based on the value of C, the output must be as given below.

The value of C can be one among the following - yYnN.
When the input is y or Y, then the output must be yes.
When the input is n or N, then the output must be no.
When the input is any other value, the output must be invalid.

'''
#Your code below

c=int(input())

if c=='y' and c=='Y':
    print("yes")
elif c=='n' and c=='N':
    print("no")
else:
    print("invalid")