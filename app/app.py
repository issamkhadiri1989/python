import numpy as np

temperatures = np.array([20, 23, 21, 20, 19, 20, 22, 23, 21, 20])

moyenne = np.mean(temperatures)
print("la moyenne est :", moyenne)

maximum = np.max(temperatures)
print("le maximum est :", maximum)

minimum = np.min(temperatures)
print("le minimum est :", minimum)