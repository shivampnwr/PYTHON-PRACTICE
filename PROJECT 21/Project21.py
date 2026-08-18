# prime checker
def primechecker(n):
    if n < 2 :
        return  False
        
    for i in range(2,n):
        if(n%i==0):
            return False
            break
    return True
    
            
  
num = int(input("enter the number:"))

if primechecker(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")

# largest using args
def largest(*args): #positional argumnets,args is like list
    return (max(args))
num = largest(12,23.23,341.23,43)
print(num)

# student information using kwargs
def studentinfo(**kwargs):  #keywords arguments,kwargs is like dictionary
    print(kwargs)
studentinfo(Name="Alice",Rollno=1,Course ="B.tech",Branch="CSE")

# challenge
def lmethods(num):
    print(max(num))
    print(min(num))
    print(sum(num))
    print(sum(num)/len(num))
numbers = list(map(int,input("enter the number in the list").split())) #take user  (int)input in the list
lmethods(numbers)
    

    



