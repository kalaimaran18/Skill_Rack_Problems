'''
Fill in the Missing lines of code so that the Program Prints the two input strings separated by a Space.

Example Input/Output

Input:

Arnold
Schwarzenegger

Output:
    Arnold Schwarzenegger

'''

def printname(firstname,lastname):
    print(firstname+" "+ lastname)

str1=input().strip()
str2=input().strip()
printname(firstname=str1, lastname=str2)