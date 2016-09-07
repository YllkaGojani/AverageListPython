def average():
    a = [1, 2, 5, 10, 255, 3]
    sum = 0
    for i in range(0, len(a)):
        sum = sum + a[i]
    print sum    
    print sum/len(a)    
        
average()  