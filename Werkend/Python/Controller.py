import numpy as np
import control as ct

## Variables
g = 9.81
l = 0.5 #m
m = 0.5 #kg


## ABCD Matrices
A = np.array([[ 0 , -g/l], [1, 0]]);

B = np.array([[0],[1/(m*l)]]);

C = np.array([[0, 1]]);

D = np.array([0]);

## Q matrix en R matrix

Q = np.array([[1, 0],
              [0, 1]]);

R = np.array([[1]]);

#Maak het systeem
sys = ct.ss(A, B, C, D);

#Definieer inputs en outputs en states

states = ["theta_dot", "theta"]
inputs = ["Fmotor1"]
outputs = ["theta"]

#Bereken de K-matrix
K, _, _ = ct.lqr(A, B, Q, R);

#Bereken de nieuwe A en B matrixen
A_aug = A - B@K

#Nieuw LQR systeem: 
syslqr = ct.ss(A_aug, B, C, D, states=states, input=inputs, output=outputs); 
print(syslqr);

#Check of reachable

# Calculate the controllability matrix
Cm = ct.ctrb(A, B)

# Check if the system is reachable
rank_Cm = np.linalg.matrix_rank(Cm)
is_reachable = rank_Cm == A.shape[0]

print("Controllability Matrix:")
print(Cm)
print("Rank of the Controllability Matrix:", rank_Cm)
print("Is the system reachable?", is_reachable)

#Functie LQR die de berekening doet en de waarden voor de motorkracht teruggeeft