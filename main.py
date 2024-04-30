import numpy as np
import control as ct
#import matplotlib.pyplot as plt
#import pandas as ps
#import SymPy as simp

## Variables
g = 9.81
l = 0.5 #m
m = 0.5 #kg


## ABCD Matrices
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

Q = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]);

R = np.array([[1, 0],
              [0, 1]]);

## LQR solver
K, S, E = ct.lqr(A, B, Q, R);
print("K-matrix");
print(K);
print("S-matrix");
print(S);

## System

