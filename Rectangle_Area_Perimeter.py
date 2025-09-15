# Rectangle area and perimeter using python function.

def getperimeterarea(length,breadth):
    return(2*(length+breadth),length*breadth)

length=int(input())
breadth=int(input())
(perimeter,Area)=getperimeterarea(length,breadth)
print(perimeter)
print(Area)
