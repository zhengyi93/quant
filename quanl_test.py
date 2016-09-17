import matplotlib.pyplot as plt
from dataExtract import *

# FED
fx_usd_sgd = extract("usd sgd fx")
zero_Rates = extract("US zero rates")

plt.plot(fx_usd_sgd)

print fx_usd_sgd
