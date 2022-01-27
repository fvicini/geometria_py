import numpy as np
from scipy import io, integrate, linalg, signal
from scipy.sparse.linalg import eigs

eps = np.finfo(float).eps or np.spacing(1)

a = np.arange(1., 0.0-0.2, -0.2)

print(a)
