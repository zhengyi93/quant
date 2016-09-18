import matplotlib.pyplot as plt
from dataExtract import *

# FED
fx_usd_sgd = extract("usd/sgd fx")
zero_Rates = extract("US zero rates")
google_px = extract("google")

# plt.plot(fx_usd_sgd)


print zero_Rates
print google_px
print fx_usd_sgd

