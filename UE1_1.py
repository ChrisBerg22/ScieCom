import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
import timeit


def lower_matrix(n):
    matrix = np.random.randint(2,10, size=(n,n))
    lower_matrix = np.tril(matrix)
    return lower_matrix
    
def b_vec(n):
    return np.random.randint(2,10,size=n)
    

def tri_solve(L,b):
    L = np.array([[3,0,0], [1,5,0], [2,3,1]])
    b = np.array([3,2,1])
    x = []
    for i in range(len(b)):
        x.append(b[i])
        for j in range(i):
            x[i] = x[i] - (L[i,j]*x[j])
        x[i] = x[i]/L[i,i]
    return x
    
def timer_(n):
    times = []

    for i in range(10):

        L = lower_matrix(n)
        b = b_vec

        start = timeit.default_timer()
        answer = tri_solve(L,b)
        stop = timeit.default_timer()
        time = stop - start
        times.append(time)
        average_time = sum(times)/len(times)
        return average_time
def timer_2(n):
    times = []

    for i in range(10):
        L = lower_matrix(n)
        b = b_vec(n)

        start = timeit.default_timer
        answer = np.linalg.solve(L,b)
        stop = timeit.default_timer()
        time = stop - start
        times.append(time)
        average_time = sum(times)/len(times)
        return average_time
    
def plot():

    x = np.array([5,10,20,50,100,200,400])
    y = np.array([timer_(5),timer_(10), timer_(20), timer_(50), timer_(100), timer_(200), timer_(400)])
    y_2 = np.array([timer_(5),timer_(10), timer_(20), timer_(50), timer_(100), timer_(200), timer_(400)])
    
    plt.yscale("log")
    plt.xscale("log")
    plt.plot(x,y, 'ko-', label='tri_solve')
    plt.plot(x,y, 'ro-', label='linalg.solve')
    plt.legend()
    plt.grid()
    plt.xlabel("n")
    plt.ylabel("time s")
    plt.title("calculation time")
    print("For smaller matrices tri_solve is pretty efficient. For larger ones, however, no longer compared to numpy")

def main():
    plot()
    L = np.array([[3,0,0], [1,5,0], [2,3,1]])
    b = np.array([3,2,1])
    print(tri_solve(L,b))

if __name__ == "__main__":
    main()
    



