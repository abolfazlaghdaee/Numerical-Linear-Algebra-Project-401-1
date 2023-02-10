import math
import numpy as np
def genUh(a):
  

    norm2 = 0
    t = a.shape[0]
    
    l = [[0] for i in range(t)]
    l[0] = [1]
    for i in a:
        norm2 += i**2
        
    norm2 = math.sqrt(norm2)    
        
    if a[0] <0:
           u=   a - norm2 * np.array(l)
    elif a[0] >= 0:
        u = a+ norm2 * np.array(l)
        
    i = np.identity(t) 
    h = i -  (2*(u@ u.T)/ (u.T @ u))
    return h