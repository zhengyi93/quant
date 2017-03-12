from numpy import *
import matplotlib.pyplot as plt

B = [-1, 1]


def gen(x):
    v = 0
    for i in range(x):
        q = B[random.randint(2)]
        if v + q >= 0:
            v += q
        else:
            v += 1
    return v


#print gen(1000)

for i in range(1000):
    q = [gen(i) for x in range(100)]
    print "{:14.8g} {:14.8g}".format(mean(q), std(q))

# m = [mean([gen(y) for i in range(100)]) for y in range(1000)]
#sd = [std([gen(y) for i in range(10)]) for y in range(1000)]
#plt.plot(m, label="Mean")
#plt.plot(sd, label="Standard Deviation")
#plt.legend(loc="upper left")
#plt.show()