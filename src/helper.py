# making stuff foolproof
import os
import sys
import re   

import matplotlib.pyplot as plt                 # plotting
from matplotlib.figure import Figure            # type hinting
from collections import Counter, OrderedDict    # data processing

def fix_dirs() -> None:
    cwd = os.getcwd()
    if cwd.split(os.sep)[-1] != 'src':
        if not os.path.exists(os.path.join(cwd, 'src')):
            raise FileNotFoundError('Please work from either the parent directory "Set",',
                                    'or from "src" in order to run any files that are in "src".')
        os.chdir(os.path.join(cwd, 'src'))
        cwd = os.getcwd()
        caller = re.search(r'src(.*?).py', str(sys._getframe(1))).group(1)[1:] + '.py'
        print(f'Working directory changed to "{cwd}".',
              f'Consider running "{caller}" from "src" dir next time.\n')
    if not os.path.exists(results_dir := os.path.join(cwd, '..', 'results')):
        os.mkdir(results_dir)

def histogram(y: list[int]) -> Figure:
    fig, ax = plt.subplots()
    od = OrderedDict(sorted(dict(Counter(y)).items()))
    b = ax.bar(od.keys(), list(od.values()))
    ax.bar_label(b)
    ax.set_xticks(list(od.keys()), labels=list(od.keys()))
    return fig

def log_plot(y: list[int]) -> Figure:
    fig, ax = plt.subplots()
    ax.set_axisbelow(True)
    ax.yaxis.grid(color='gray', linestyle='dashed')
    ax.set_ylim([0, 511920])
    ax.set_xscale('log')

    x = [10**i for i in range(len(y))]
    ax.plot(x, y)
    return fig

def save_plot(fig: Figure, filename: str = None) -> None:
    if filename is None:
        filename = os.path.join(os.getcwd(), 'plot.png')
    if os.path.exists(filename):
        yn = 'placeholder'
        while yn.lower() not in 'yn':
            yn = input(f'File "\033[1m{filename.split(os.path.sep)[-1]}\033[0m" already exists.\nOverwrite? [y/n]: ')
        if yn.lower() == 'y':
            fig.savefig(filename)
    else:
        fig.savefig(filename)
