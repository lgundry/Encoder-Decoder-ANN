import numpy as np
from sklearn.datasets import make_classification

# 1: create dummy dataset and split it into class 0 and class 1 collections, stored in x0, y0 and x1, y1, respectively

a,b = make_classification(n_samples=10000, weights=(0.9,0.1))
idx = np.where(b == 0)[0]
x0 = a[idx,:]
y0 = b[idx]
idx = np.where(b == 1)[0]
x1 = a[idx,:]
y1 = b[idx]

# 2: randomize the ordering

idx = np.argsort(np.random.random(y0.shape))
y0 = y0[idx]
x0 = x0[idx]
idx = np.argsort(np.random.random(y1.shape))
y1 = y1[idx]
x1 = x1[idx]

# 3: extract the first 90% of the total in the dataset

ntrn0 = int(0.9*x0.shape[0])
ntrn1 = int(0.9*x1.shape[0])
xtrn = np.zeros((int(ntrn0+ntrn1),20))
ytrn = np.zeros(int(ntrn0+ntrn1))
xtrn[:ntrn0] = x0[:ntrn0]
xtrn[ntrn0:] = x1[:ntrn1]
ytrn[:ntrn0] = y0[:ntrn0]
ytrn[ntrn0:] = y1[:ntrn1]

# 4: 5 extracat 5% for the validation set

n0 = int(x0.shape[0]-ntrn0)
n1 = int(x1.shape[0]-ntrn1)
xval = np.zeros((int(n0/2+n1/2),20))
yval = np.zeros(int(n0/2+n1/2))
xval[:(n0//2)] = x0[ntrn0:(ntrn0+n0//2)]
xval[(n0//2):] = x1[ntrn1:(ntrn1+n1//2)]
yval[:(n0//2):] = y0[ntrn0:(ntrn0+n0//2)]
yval[(n0//2):] = y1[ntrn1:(ntrn1+n1//2)]

# 5: extract the final 5% for the test set

xtst = np.concatenate((x0[(ntrn0+n0//2):],x1[(ntrn1+n1//2):]))
ytst = np.concatenate((y0[(ntrn0+n0//2):],y1[(ntrn1+n1//2):]))