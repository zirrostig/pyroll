#!/usr/bin/env python3

import sys

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
import numpy as np

import pyroll

def main(*argv):
    #grab args
    if len(argv) < 3:
        print("Usage: pyroll_graph.py <rolls> [<dice>]")
        sys.exit(1)

    rolls = int(argv[1])
    dice = list(map(int, argv[2:]))

    #get calculated probabalities
    calc_eq = pyroll.prob_calc(dice)
    calc_lt = pyroll.less_gen(calc_eq)
    calc_gt = pyroll.greater_gen(calc_eq)

    #get simulated probabalities
    sim_eq = pyroll.sim(rolls, dice)
    sim_lt = pyroll.less_gen(sim_eq)
    sim_gt = pyroll.greater_gen(sim_eq)

    #setup matplotlib
    fig = plt.figure()
    fig.subplots_adjust(wspace=0.05, hspace=0.05)
    gs = GridSpec(1, 7)
    gs.update(left=0.05, right=0.95, wspace=0.05)

    #plot eq_probs
    eq_ax = fig.add_subplot(gs[:, 2:-2], projection='3d')
    eq_x = np.arange(len(dice), sum(dice) + 1)
    eq_ax.set_title('Roll ==')
    eq_ax.set_yticks([0,1])
    eq_ax.set_yticklabels([])
    eq_ax.set_xticks(eq_x[::2])
    eq_ax.set_xlabel("Roll")
    eq_ax.set_zlabel("Prob")
    eq_ax.set_ylim3d(-4,1)
    eq_ax.view_init(elev=4, azim=-90)
    #eq_calc
    eq_z = np.array([calc_eq.get(i, 0) for i in range(len(dice), sum(dice) + 1)])
    cs = ['b'] * len(eq_x)
    eq_ax.bar(eq_x, eq_z, zs=1, zdir='y', color=cs, alpha=0.75)
    #eq_sim
    eq_z = np.array([sim_eq.get(i, 0) for i in range(len(dice), sum(dice) + 1)])
    cs = ['r'] * len(eq_x)
    eq_ax.bar(eq_x, eq_z, zs=0, zdir='y', color=cs, alpha=0.6)

    #plot lt_plobs
    lt_ax = fig.add_subplot(gs[:, :2], projection='3d')
    lt_x = np.arange(len(dice), sum(dice) + 1)
    lt_ax.set_title("Roll <")
    lt_ax.set_yticks([0,1])
    lt_ax.set_yticklabels([])
    lt_ax.set_xticks(lt_x[::4])
    lt_ax.set_ylim3d(-4,1)
    lt_ax.set_zlim3d(0,1)
    lt_ax.view_init(elev=4, azim=-90)
    #lt_calc
    lt_z = np.array([calc_lt.get(i, 0) for i in range(len(dice), sum(dice) + 1)])
    cs = ['b'] * len(lt_x)
    lt_ax.bar(lt_x, lt_z, zs=1, zdir='y', color=cs, alpha=0.75)
    #lt_sim
    lt_z = np.array([sim_lt.get(i, 0) for i in range(len(dice), sum(dice) + 1)])
    cs = ['r'] * len(lt_x)
    lt_ax.bar(lt_x, lt_z, zs=0, zdir='y', color=cs, alpha=0.6)

    #plot gt_plobs
    gt_ax = fig.add_subplot(gs[:, -2:], projection='3d')
    gt_x = np.arange(len(dice), sum(dice) + 1)
    gt_ax.set_title("Roll >")
    gt_ax.set_yticks([0,1])
    gt_ax.set_yticklabels([])
    gt_ax.set_xticks(gt_x[::4])
    gt_ax.set_ylim3d(-4,1)
    gt_ax.set_zlim3d(0,1)
    gt_ax.view_init(elev=3, azim=-90)
    #gt_calc
    gt_z = np.array([calc_gt.get(i, 0) for i in range(len(dice), sum(dice) + 1)])
    cs = ['b'] * len(gt_x)
    gt_ax.bar(gt_x, gt_z, zs=1, zdir='y', color=cs, alpha=0.75)
    #gt_sim
    gt_z = np.array([sim_gt.get(i, 0) for i in range(len(dice), sum(dice) + 1)])
    cs = ['r'] * len(gt_x)
    gt_ax.bar(gt_x, gt_z, zs=0, zdir='y', color=cs, alpha=0.6)


    # print(calc_eq)
    # print(calc_lt)
    # print(calc_gt)

    # print(sim_eq)
    # print(sim_lt)
    # print(sim_gt)

    plt.show()


if __name__ == '__main__':
    main(*sys.argv)
