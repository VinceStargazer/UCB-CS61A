from math import log, sqrt

r1, r2, n1, n2 = 0.696, 0.29, 272, 346
zr = lambda r: 0.5 * log((1+r)/(1-r))
zd = (zr(r1) - zr(r2)) / sqrt((1 / (n1-3)) + (1 / (n2-3)))
print(zd)
