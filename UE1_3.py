import numpy as np
import matplotlib.pyplot as plt

mu = -1  #[eV]
k_b = 8.6173324e-5 #[eV/K]


def FD(e,T):
    '''Fermi Dirac Distribution '''
    return 1/(np.exp((e-mu)/(k_b*T)) + 1)

def p(e,T):
    '''Probability of unoccupied states '''
    return 1 - FD(e,T)

def plot():
    e = np.linspace(-3,0,100)
    f_1 = p(e,10)
    f_2 = p(e,300)
    f_3 = p(e,1000)

    plt.plot(e,f_1,label = '10K')
    plt.plot(e,f_2,label = '300K')
    plt.plot(e,f_3,label = '1000K')
    plt.legend()
    plt.grid()
    plt.xlabel("e [eV]")
    plt.ylabel("1 - f(e)")
    plt.title("Probability of unoccupied states")

def p_new(e,T):
    return np.exp((e-mu)/(k_b*T))/(np.exp((e-mu)/(k_b*T))+1)

def table_():
    ''' Makes table with the zeroth column being energy, first column being p1 values, and third being p2 values '''
    e_val = np.arange(-3,0,0.2)
    values = p(e_val,300)
    values_new = p_new(e_val,300)
    table = np.vstack((e_val,values,values_new)).T
    return table

def main():
    plot()
    print(table_())
    print("The two results differ, because in the second version we got rid of the subtraction of similar numbers.")

if __name__ == "__main__":
    main()



