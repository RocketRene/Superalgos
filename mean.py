    
def mean(x):  
    
    sum = 0
    for i in x:
        sum = sum + i
    mean = sum/len(x)
    print(mean)
x = [1,2,3,4,5,6,7]
mean(x)