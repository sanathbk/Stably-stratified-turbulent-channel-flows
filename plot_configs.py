

def custom_formatter(x, pos):
    if abs(x - round(x)) < 1e-6:
        return rf'${int(round(x))}$'
    else:
        return rf'${x:.1f}$'

def set_plot_params(use_tex=False):

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import integrate
    from matplotlib import rc, rcParams
    from matplotlib.ticker import ScalarFormatter, NullFormatter, MultipleLocator, AutoMinorLocator, FuncFormatter
    import cmocean

    fig_width_pt  = 426.79134
    inches_per_pt = 1.0 / 72.27
    aspect_ratio  = 0.70
    fig_scale     = 1.0
    fig_width     = fig_width_pt * inches_per_pt * fig_scale
    fig_height    = fig_width * aspect_ratio
    fig_size      = [fig_width, fig_height]

    rc('text', usetex=use_tex)
    rcParams.update({
        'figure.figsize': fig_size,
        "xtick.major.size": 6, "xtick.minor.size": 3,
        "ytick.major.size": 6, "ytick.minor.size": 3,
        'xtick.direction': 'in', 'ytick.direction': 'in',
        'ytick.minor.visible': True, 'xtick.minor.visible': True,
        'xtick.top': True, 'ytick.right': True,
        'font.size': 18,
        'figure.constrained_layout.use': True
    })

    return 0

__all__ = ['set_plot_params', 'custom_formatter']
