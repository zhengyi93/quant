import matplotlib.pyplot as plt
from quandlDataExtract import *

# FED
fx_usd_sgd = extract("usdsgd fx")
zero_Rates = extract("US zero rates")

plt.plot(fx_usd_sgd)

print fx_usd_sgd
