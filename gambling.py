# Simulation of the gambling strategy of betting twice every lost game
from random import randint

trials = 10000000
principle = 2**10
results = []

for i in range(trials):
    cash = principle
    bet = 1
    for j in range(30):
        outcome = randint(0, 1)
        if outcome:
            cash += bet
            bet = 2
        else:
            cash -= bet
            if not cash or 2*bet > cash:
                break
            else:
                bet *= 2
    results.append(-principle + cash)


f = open('data.csv', 'w')

f.write(','.join(map(str, results)))

print sum(results)/float(len(results))
