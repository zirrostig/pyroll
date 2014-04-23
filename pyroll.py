import random
import itertools
from functools import reduce
import operator


def roll(*sides):
    total = 0
    for s in sides:
        total += random.randint(1,s)

    return total

def prob_calc(dice):
    p = 0
    rolls = itertools.product(*map((lambda d: range(1, d+1)), dice))
    num_rolls = reduce(operator.mul, dice)
    hits = {}
    for r in rolls:
        s = sum(r)
        if s in hits:
            hits[s] += 1
        else:
            hits[s] = 1

    return { s : (h/num_rolls) for s, h in hits.items() }

def prob(target, rolls, dice):
    hits = 0
    for i in range(rolls):
        if roll(*dice) == target:
            hits += 1

    return hits / rolls

def sim(rolls, dice):
    min_roll = len(dice)
    max_roll = sum(dice)

    probs = {}
    for t in range(min_roll, max_roll+1):
        p = prob(t, rolls, dice)
        probs[t] = p

    return probs

def less_gen(probs):
    probs_lt = {}
    total = 0
    for s in range(max(probs)):
        if s not in probs:
            continue
        probs_lt[s] = total
        total += probs[s]

    return probs_lt

def greater_gen(probs):
    probs_gt = {}
    total = 0
    for s in range(max(probs), 0, -1):
        if s not in probs:
            continue
        probs_gt[s] = total
        total += probs[s]

    return probs_gt

