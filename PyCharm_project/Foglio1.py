# imports
import matplotlib.pyplot as plt
import numpy as np

######################################################################
# ES 2 FOGLIO 1


def espressione_con_cn(x):
    return (np.exp(x)-1)/x

def espressione_esatta(x, n):
    sviluppo = 0.
    # sommatoria da 1 a x^(n-1)/n!
    for i in range(1, n+1):
        sviluppo += x**(i-1)/np.math.factorial(i)
    return sviluppo

x = np.asarray([10**(-n) for n in range(1, 17)])
y = espressione_con_cn(x)
y_true = espressione_esatta(x, 15)
errore = np.abs(y-y_true)/np.abs(y_true)

data = np.stack([x, y, y_true, errore], axis=1)
print("Errore cancellazione numerica:\n", data)

plt.xscale('log')
plt.yscale('log')
plt.title("Errore cancellazione numerica")
plt.xlabel("x")
plt.ylabel("Errore")
plt.scatter(x, errore)
plt.show()

######################################################################
# ES 4 FOGLIO 1

def rapporto_incrementale(x, h):
    return (np.sin(x+h) - np.sin(x))/h

def espressione_modificata(x, h):
    return 2 * np.sin(h/2) * np.cos(x+h/2) / h

h = np.asarray([2**(-k) for k in range(1,51)])
x = np.pi/4
derivata_esatta = np.cos(x)

derivata_rapp_increm = rapporto_incrementale(x, h)
errore_rapporto_incrementale = np.abs(derivata_rapp_increm - derivata_esatta) / np.abs(derivata_esatta)

plt.xscale('log')
plt.yscale('log')
plt.title("Errore rapporto incrementale")
plt.xlabel("x")
plt.ylabel("Errore")
plt.scatter(h, errore_rapporto_incrementale)
plt.show()

derivata_espress_modificata = espressione_modificata(x, h)
errore_espress_modificata = np.abs(derivata_espress_modificata - derivata_esatta) / np.abs(derivata_esatta)

plt.xscale('log')
plt.yscale('log')
plt.title("Errore espressione_modificata")
plt.xlabel("x")
plt.ylabel("Errore")
plt.scatter(h, errore_espress_modificata)
plt.show()
