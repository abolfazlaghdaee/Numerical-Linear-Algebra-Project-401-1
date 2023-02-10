import numpy as np
def gen_H(a):
    n = a.shape[0]
    H = a
    
    
    for i in range(n, 10):
        c = np.array([[0 for i in range(n)]])
        c2 = np.array([ 0 for i in range(n+1)])

        f = np.append(c , H, axis =0)
        H = np.insert(f, 0 , c2, axis = 1)
        H[0,0] =1 


        if H.shape[0] == 10:
            return H

        else: 
            return gen_H(H)
