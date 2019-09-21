import numpy as np # import numpy to use numpy functions like power function 
import math #  to calcualte mathematical functions math library is imported
import time ## timeit will show the time proecessing how  long it tale to execute the code. 
import matplotlib.pyplot as plt
from time import clock
from scipy.linalg import eigh as largest_eigh
from scipy.sparse.linalg.eigen.arpack import eigsh as largest_eigsh
#import sys # system efficieny is used to calcualte functinos 
size = (1000) #   to calcualte total time taken to process the edxcution of this code. *1000 means we want to 
# to know the time taken to execute the code in mili seconds 
# implementation 3 approach. 
N = int(input('Please enter the diemention you want (N*N):'))
N = (N)
d = np.random.random((N,N)) -0.5

print(d)
start = time.time()
print((time.time()-start)*500)# this is the similar way to implement the mehtod like it has been 
# implemented twice in this code see below to find other eigh and eigsh values and iterations to 
# compute the total time consumded to calculate largest values of eigenvalues and eigenvectors. 
print("d :  \n",d)
# now we will find out the eigenvalues of 4 by 4 matrix 
print("Eigenvalues :", np.linalg.eigvals(d))
# to find eigenvectors of the n by n matrix we will use eigenvector method. 
eigenvalue,eigenvector = np.linalg.eig(d)
print("First tuple of eig:", eigenvalue)
print("Second tuple of eig:", eigenvector)
start = time.time()
print((time.time()-start)*100)

tol = int(input('input error tolerance (tol): ')) # to get input error tolerance, greater values and 
# more tolerance erros to computing values of the tolerance. 
start = time.time()
print((time.time()-start)*100)
# Using dot product we implement the new method 
 
np.set_printoptions(suppress=True)
np.random.seed(3)# to calculate the values of time with random seed in this case we have given
# 0 and we can chnage it to many other things like. let sy to value 2 or we can implement for loop
# to iterate the function and get required values. 
N=5000
k=10
X = np.random.random((N,N)) - 2.5
X = np.dot(X, X.T) #create a symmetric matrix

# Benchmark the dense routine
start = clock()
evals_large, evecs_large = largest_eigh(X, eigvals=(N-k,N-1))
elapsed = (clock() - start)
print("eigh elapsed time: ", elapsed)
print(X)
# Benchmark the sparse routine
start = clock()
evals_large_sparse, evecs_large_sparse = largest_eigsh(X, k, which='LM')
elapsed = (clock() - start)
print("eigsh elapsed time: ", elapsed)

#################333

# approach 2 Numpy universial functions
import numpy as np
import time
import sys # library to see the memoray occupied by list and numpy array. 
N = int(input('Please enter the diemention you want (N*N):'))
N = (N)
d = np.random.random((N,N)) -0.5

print(d)
start = time.time()
print((time.time()-start)*500)

s = range(1000)
print(sys.getsizeof(5)*len(s))# printing sizeof s 
D = np.arange(1000)
print(D.size*D.itemsize)# printing sizeof numpy array 

SIZE = 1000000# to see how long it tak etime to reach the result
List1 = range(SIZE)
List2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()

result = [(x, y) for x,y in zip(List1, List2)]

start = time.time()
result = A1+A2
print((time.time()-start)*10)
# matrix dot product with numpy class
y = [N]
x = [N]
dot_product1 = np.dot(x,y)
print('Dot product is : ' , dot_product1)
# Now we can implement it without using numpy 
dot_product2 = 0
for i, j in zip(x,y): # using for loop we calculates this
    dot_product2 += i*j
    print('Dot product is:', dot_product2)
    print((time.time()-start)*1000)


################################################

section 3 

import numpy as np
import time
N = int(input('Please enter the diemention you want (NbyN):'))
N = (N)
d = np.random.random((N,N)) -1.5 # random method is used to enter the diemension of higher vectors.
start = time.time()
print((time.time()-start)*1000)
print(d)
a = np.array([d +2j,d +4j])
b = np.array([d +6j,d +8j])
y = np.vdot(a, b)
x = np.vdot(b, a)
print(x, y)
print((time.time()-start)*1000)

# division of matrices in this esction, which defines the values of the functions
x1 = np.arange(N).reshape((N))
x2 = np.arange(N)
r = np.multiply(x1, x2)
print(r)
print((time.time()-start)*1000)
