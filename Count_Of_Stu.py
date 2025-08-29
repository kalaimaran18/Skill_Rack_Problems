'''
Certain number of students appear for an exam and their marks are passed as the input to the program.
The marks are separated by a space. The maximum marks that can be obtained in the exam is 100.
Fill in the lines of code so that the program prints the total count of students who have scored 50 or 100.

'''

mark=list(map(int,input().split(" ")))
print(mark.count(50)+mark.count(100))