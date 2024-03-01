import argparse
import random
import numpy as np


NUM_SIMULATIONS = 1_000_000
# NUM_SIMULATIONS = 100_000
# NUM_SIMULATIONS = 1000
MAX_ROLLS = 1000

parser = argparse.ArgumentParser()
parser.add_argument('chain', type=int, nargs='+')
args = parser.parse_args()

DICE_CHAIN = args.chain
MAX_CHAIN_STATE = len(DICE_CHAIN) - 1

results = []
timed_out = 0

for _ in range(NUM_SIMULATIONS):
    chain_state = 0
    rolls = 0
    while True:
        if rolls == MAX_ROLLS:
            results.append(rolls)
            timed_out += 1
            break
        current_die = DICE_CHAIN[chain_state]
        x = random.randint(1, current_die)
        rolls += 1
        if x == 1:
            if chain_state == MAX_CHAIN_STATE:
                results.append(rolls)
                break
            else:
                chain_state += 1
        
print(f'Dice chain: {DICE_CHAIN}')        
avg = sum(results) / len(results)
print(f'Average: {avg}')
for i in range(25):
    p = i + 1
    print(f'{p} percentile: {np.percentile(results, p)}')

print(f'50th percentile: {np.percentile(results, 50)}')
print(f'Timed out: {timed_out}')
hist = np.histogram(results)
