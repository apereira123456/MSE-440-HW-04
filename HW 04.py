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
plt.plot([0,0], [-1,1], color='k')
plt.plot([0,10], [0,0], color='k')
plt.plot([22,32], [0,0], color='k')
plt.plot([32,32], [-1,1], color='k')
plt.plot([32,64], [0,0], color='k')
plt.plot([76,108], [0,0], color='k')
plt.plot([108,108], [-1,1], color='k')
plt.plot([108,164], [0,0], color='k')
plt.plot([176,233], [0,0], color='k')
plt.plot([233,233], [-1,1], color='k')

plt.annotate(r'$R_3$', xy=(16, 0), ha='center', va='center')
plt.annotate(r'$R_2$', xy=(70, 0), ha='center', va='center')
plt.annotate(r'$R_1$', xy=(170, 0), ha='center', va='center')
    
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
plt.plot([0,0], [-1,1], color='k')
plt.plot([0,10], [0,0], color='k')
plt.plot([22,32], [0,0], color='k')
plt.plot([32,32], [-1,1], color='k')
plt.plot([32,45], [0,0], color='k')
plt.plot([57,70], [0,0], color='k')
plt.plot([70,70], [-1,1], color='k')
plt.plot([70,125], [0,0], color='k')
plt.plot([137,192], [0,0], color='k')
plt.plot([192,192], [-1,1], color='k')

plt.annotate(r'$R_3$', xy=(16, 0), ha='center', va='center')
plt.annotate(r'$R_2$', xy=(51, 0), ha='center', va='center')
plt.annotate(r'$R_1$', xy=(131, 0), ha='center', va='center')
    
plt.title('Sample 2')
plt.xlabel(r'$Z_{real}$')
plt.ylabel(r'$-Z_{imag}$')

fig_2.savefig('sample 2.png')