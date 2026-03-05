
import numpy as np
import pandas as pd
import re
from random import shuffle
import sys, os, h5py
import shutil
import pathlib

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D
from mpl_toolkits.axes_grid1.inset_locator import (inset_axes,InsetPosition,mark_inset)
from matplotlib.legend_handler import HandlerTuple
from matplotlib import patheffects
from matplotlib import rc, rcParams
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FuncFormatter

from scipy import integrate
import seaborn as sns
import cmocean

fig_width_pt  = 426.79134                            # \showthe\columnwidth
inches_per_pt = 1.0/72.27                            # pt to in
aspect_ratio  = 0.70                                 # aspect ratio
fig_scale     = 1.0                                  # scale factor
fig_width     = fig_width_pt*inches_per_pt*fig_scale # width in in
fig_height    = fig_width*aspect_ratio               # height in in
fig_size      = [fig_width,fig_height]


def custom_formatter(x, pos):
    if abs(x - round(x)) < 1e-6:
        return rf'${int(round(x))}$'
    else:
        return rf'${x:.1f}$'   


rc('text', usetex=True)  # switch to True for latex font (might be slow)
rcParams.update({'figure.figsize': fig_size, "xtick.major.size": 6, "xtick.minor.size": 3, "ytick.major.size": 6, "ytick.minor.size": 3, 
                 'xtick.direction': 'in', 'ytick.direction': 'in', 'xtick.top': True, 'ytick.right': True, 
                 'font.size': 18, 'figure.constrained_layout.use':True})
rcParams['ytick.minor.visible'] = True
rcParams['xtick.minor.visible'] = True

greys   = [plt.get_cmap("Greys"  , 16)(i) for i in range(1, 15)]
blues   = cmocean.tools.crop_by_percent(cmocean.cm.balance_r, 50, which='min', N=10)
reds    = cmocean.tools.crop_by_percent(cmocean.cm.balance, 50, which='min', N=10)
greens  = cmocean.tools.crop_by_percent(cmocean.cm.algae, 50, which='min', N=10)
purples = cmocean.tools.crop_by_percent(cmocean.cm.amp, 10, which='min', N=10)
greens