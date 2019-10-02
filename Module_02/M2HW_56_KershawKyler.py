"""
Kyler Kershaw

Define a function "rotate" that recieves three arguments and returns
a tuple in which the first argument is at index 1, the second argument
is at index 2, and the third argument is at index 0. Define variables 
a, b, and c containing "Doug",  22 and 1984. Then call the function three
times. For each call, unpack its result into a, b, and c, then display
their values. 
"""

def rotate(a, b, c):
    """
    This function is given three variables and rotates them.
    """
    dataList = (a, b, c)
    print(dataList)
    
    for count in range(3):
        temp = a
        temp2 = b
        a=c
        b=temp
        c=temp2
        dataList = (a, b, c)
        print(dataList)
    
    


def main():
    
    a = "Doug"
    b = "22"
    c = "1984"
    
    rotate(a, b, c)
    

main()