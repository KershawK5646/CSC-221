# coding: utf-8
import numpy as np
import pandas as pd
temps = np.random.randint(60,101,6)
temperatures = pd.Series(temps)
temperatures
temperatures.min()
temperatures.max()
temperatures.mean()
temperatures.describe()
