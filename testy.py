#Random noise number average generator.



import numpy as np
import time

import matplotlib.pyplot as plt



# noise = PerlinNoise(octaves=10, seed=1)
# xpix, ypix = 100, 100
# pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

# plt.imshow(pic, cmap='gray')
# plt.show()

outputs = []

start = time.time()
for i in range(2):
    for i in range(10000000):
        noise = np.random.lognormal(0, 1, 1)
        while (round(noise[0], 5) == 0.0):
            noise = np.random.lognormal(0, 5, 100)
        outputs.append(round(noise[0], 5))
        #print(f" Iternation {i} -- {(round(noise[1], 5))}")
        
    x = 0.
    print("\n Calculating...\n")

    # for i in range(len(outputs)):
    #     x += outputs[i]
    #     print(f"\n X: {x} -- \n")
    average = sum(outputs) / len(outputs)


    print("\n\n - - - - -\n\n")
    print(f"Output Average is: {average}")
    print(f"Calculation {i} time: {time.time() - start}sec")
    print("\n\n - - - - -\n\n.")

print(f"\n\n\nFull Calculation time: {time.time() - start}seconds")
