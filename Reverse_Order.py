# Reverse the number print till the particular Range

M=int(input())
N=int(input())
X=int(input())
for i in range(N,M-1,-1):
    if i%X==0:
        print(i,end=" ") 