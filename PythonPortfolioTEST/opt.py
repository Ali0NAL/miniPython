import os
import numpy as np

# Dosya yolunu doğrudan belirtin
filename = r'C:\Users\app_a\Documents\Python Projects\miniPython\SRC\veri.xlsx'

# Geri kalan kod aynı kalır
data = np.genfromtxt(filename, skip_header=1, usecols=36, max_rows=83, encoding='ISO-8859-9')


# ... (kodun geri kalanı)



pn = 20
maxiter = 20000
wmin = 0
wmax = 0.03

yas = data.shape[1]
OPT = np.zeros((pn, yas + 3))

for i in range(pn):
    w = np.zeros((yas, 1))
    w[yas - 1, 0] = -1
    while w[yas - 1, 0] < 0:
        for j in range(yas - 1):
            w[j, 0] = wmin + np.random.rand() * (wmax - wmin)
        w[yas - 1, 0] = 1 - np.sum(w[0:(yas - 1), 0])

    ER = np.sum(w * np.mean(data, axis=0))

    C = np.cov(data, rowvar=False)
    STD = np.zeros((yas, 1))

    for st1 in range(yas):
        for st2 in range(yas):
            if st1 == st2:
                STD[st1, 0] += C[st1, st2] * w[st1, 0] * w[st2, 0]
            else:
                STD[st1, 0] += 2 * C[st1, st2] * w[st1, 0] * w[st2, 0]

    STSapma = np.sqrt(np.sum(STD[:, 0]))

    Tx = ER / STSapma

    OPT[i, 0: yas] = w.flatten()
    OPT[i, yas] = ER
    OPT[i, yas + 1] = STSapma
    OPT[i, yas + 2] = Tx

OPT1 = np.zeros((pn, yas + 3))

for i in range(pn):
    w = OPT[i, 0:yas].reshape(yas, 1)

    if w[yas - 1, 0] < 0.001:
        w[yas - 1, 0] = 0

    ER = np.sum(w * np.mean(data, axis=0))

    C = np.cov(data, rowvar=False)
    STD = np.zeros((yas, 1))

    for st1 in range(yas):
        for st2 in range(yas):
            if st1 == st2:
                STD[st1, 0] += C[st1, st2] * w[st1, 0] * w[st2, 0]
            else:
                STD[st1, 0] += 2 * C[st1, st2] * w[st1, 0] * w[st2, 0]

    STSapma = np.sqrt(np.sum(STD[:, 0]))

    Tx = ER / STSapma

    if np.any(w < 0):
        fx = -1e-6

    OPT1[i, 0: yas] = w.flatten()
    OPT1[i, yas] = ER
    OPT1[i, yas + 1] = STSapma
    OPT1[i, yas + 2] = Tx

for i in range(pn):
    if OPT[i, yas + 2] < OPT1[i, yas + 2]:
        OPT[i, :] = OPT1[i, :]

v1 = np.ceil(np.random.rand(pn))
v2 = np.ceil(np.random.rand(pn))

while np.array_equal(v1, v2):
    v1 = np.ceil(np.random.rand(pn))
    v2 = np.ceil(np.random.rand(pn))

for j in range(yas - 1):
    OPT[:, j] = OPT[:, j] + np.random.rand(pn) * (OPT[v1.astype(int), j] - OPT[v2.astype(int), j])

OPT[:, yas - 1] = 1 - np.sum(OPT[:, 0:(yas - 1)], axis=1)

for j in range(yas):
    OPT[:, j] = np.where(OPT[:, j] < 0.001, 0, OPT[:, j])

for i in range(pn):
    w = OPT[i, 0:yas].reshape(yas, 1)

    if np.any(w < 0):
        fx = -1e-6

    OPT1[0, 0:yas] = w.flatten()
    OPT1[0, yas] = ER
    OPT1[0, yas + 1] = STSapma
    OPT1[0, yas + 2] = Tx

for i in range(pn):
    if OPT[i, yas + 2] < OPT1[i, yas + 2]:
        OPT[i, :] = OPT1[i, :]

