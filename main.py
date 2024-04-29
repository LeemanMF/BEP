import numpy as np
import control as ct
#import matplotlib.pyplot as plt
#import pandas as ps
#import SymPy as simp

## Variables
g = 9.81
l = 0.5 #m
m = 5 #kg
## Control matrices
A = np.array([[0, 0, 1, 0],
             [0, 0, 0, 1],
             [0, -(g/l), 0,0],
             [-(g/l), 0, 0, 0]]);

B = np.array([[0, 0],
             [0, 0],
             [(1/m), 0],
             [0, (1/m)]]);

C = np.array([[1, 0, 0, 0],
             [0, 1, 0, 0]]);

D = np.array([0]);

## Q matrix en R matrix

Q = np.identity(4);

R = np.identity(2);



## LQR solver
K, S, E = ct.lqr(A, B, Q, R);

print(K);
