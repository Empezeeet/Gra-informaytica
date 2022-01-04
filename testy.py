import numpy as np
import time
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt

# noise = PerlinNoise(octaves=10, seed=1)
# xpix, ypix = 100, 100
# pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

# plt.imshow(pic, cmap='gray')
# plt.show()

outputs = []



for i in range(100000):
    noise = np.random.lognormal(0, 1, 10)
    while ('e' in str(round(noise[1], 5))) or (round(noise[1], 5) == 0.0):
        noise = np.random.lognormal(0, 5, 100)
    outputs.append(round(noise[1], 5))
    print((round(noise[1], 5)) * 10)
    
x = 0.
print("\n Calculating...\n")

for i in range(len(outputs)):
    x += outputs[i]
    print(f"\n X: {x} -- \n")
print("\n\n - - - - -\n\n")
print((x/len(outputs)) * 0.1)
print("\n\n - - - - -\n\n.")


