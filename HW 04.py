import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def semicircle(center_x, center_y, r):
    theta = np.linspace(0, np.pi, 100)
    x = r * np.cos(theta) + center_x
    y = r * np.sin(theta) + center_y
    
    return x, y

## Sample 1

sample_1 = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-440-HW-04\sample 1.csv')

w1 = sample_1.iloc[:, 0]
Z1 = sample_1.iloc[:, 1]
p1 = sample_1.iloc[:, 2]

X1 = Z1 * np.cos(p1 / 180 * np.pi)
Y1 = Z1 * np.sin(p1 / 180 * np.pi)

X1_Rs, Y1_Rs = semicircle(70,0,38)
X1_Rl, Y1_Rl = semicircle(170,0,63) 

fig_1 = plt.figure(dpi=300)
plt.scatter(X1, Y1, color='C0')
plt.plot(X1_Rs, Y1_Rs, color='C1')
plt.plot(X1_Rl, Y1_Rl, color='C2')
    
plt.title('Sample 1')
plt.xlabel(r'$Z_{real}$')
plt.ylabel(r'$-Z_{imag}$')

fig_1.savefig('sample 1.png')

## Sample 2

sample_2 = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-440-HW-04\sample 2.csv')

w2 = sample_2.iloc[:, 0]
Z2 = sample_2.iloc[:, 1]
p2 = sample_2.iloc[:, 2]

X2 = Z2 * np.cos(p2 / 180 * np.pi)
Y2 = Z2 * np.sin(p2 / 180 * np.pi)

X2_Rs, Y2_Rs = semicircle(51,0,19)
X2_Rl, Y2_Rl = semicircle(131,0,61)

fig_2 = plt.figure(dpi=300)
plt.scatter(X2, Y2, color='C3')
plt.plot(X2_Rs, Y2_Rs, color='C4')
plt.plot(X2_Rl, Y2_Rl, color='C5')
    
plt.title('Sample 2')
plt.xlabel(r'$Z_{real}$')
plt.ylabel(r'$-Z_{imag}$')

fig_2.savefig('sample 2.png')