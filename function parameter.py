
#arithematic operation 
"""
def demo(x,y):
    a= 12
    b= 13
    print(x+y)
    print('pre def val',a+b)
    print("prasanna")
demo(12,12)
demo(20,20)

"""
# default parameter and return 
# default parameter vlaue declare
#  as right only ex:
def demo(name,id=200):
    print(name)
    print(id)

demo("prasanna") #o/p is prasanna 200 
#wrong method and error 
# default parameter vlaue declare
#  as right only ex:
def demo(id=200,name):
    print(name)
    print(id)

demo("prasanna") #o/p is   
# File "/home/prasanna/Documents/python3/python basic/function parameter.py", line 24
 #   def demo(id=200,name):
#SyntaxError: non-default argument follows default argument
 

