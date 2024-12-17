# importing libraries
import pandas as pd
import scipy
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
import time

lst = [i for i in range(1000000)]
start = time.time()
sum_lst = [x + 1 for x in lst]
end = time.time()
print("List Time:", end - start)

arr = np.array(lst)
start = time.time()
sum_arr = arr + 1
end = time.time()
print("Array Time:", end - start)