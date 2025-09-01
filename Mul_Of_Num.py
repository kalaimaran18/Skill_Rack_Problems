'''
A number N is passed as input. Another number X is also passed as input. The program must print first X multiples of the number N.

Input Format:

The first line denotes the value of N
The second line denotes the value of X

Output Format:
The first X multiples of N, each separated by a space.

'''

n=int(input())
x=int(input())
for i in range(1,x+1):
    print(n*i,end=" ")