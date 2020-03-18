#!/usr/bin/env python
# A. Pohl, Jan 16 2020
# Plots genie time series


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import warnings
from sklearn.linear_model import LinearRegression
import pandas as pd
import textwrap
import netCDF4
from netCDF4 import Dataset

##########################

indir= '/archive/crct/al1966po/Phanerozoic_GENIE/OSCILLATIONS/genie_output/ww_long_runs'
#exps = ['AP.445eb12X.PO4.1.0O2.TdepJohn2014.1.0PO4_saveslicesforcycles.SPIN']
exps = ['muffin.CB.eg_ww_hi.BASES.4.0X.SPIN']
#exps = ['AP.445eb24X.PO4.1.0O2.TdepJohn2014.1.0PO4.SPIN','AP.445eb17X.PO4.1.0O2.TdepJohn2014.1.0PO4.SPIN','AP.445eb12X.PO4.1.0O2.TdepJohn2014.1.0PO4.SPIN','AP.445eb10X.PO4.1.0O2.TdepJohn2014.1.0PO4.SPIN','AP.445eb8.5X.PO4.1.0O2.TdepJohn2014.1.0PO4.SPIN','AP.445eb7X.PO4.1.0O2.TdepJohn2014.1.0PO4.SPIN','AP.445eb6X.PO4.1.0O2.TdepJohn2014.1.0PO4.SPIN','AP.445eb5X.PO4.1.0O2.TdepJohn2014.1.0PO4.SPIN']
#exps = ['AP.445eb17X.PO4.1.0O2.TdepJohn2014.1.0PO4.SPIN','AP.445eb17X.PO4.0.4O2.TdepJohn2014.1.0PO4.SPIN','AP.445eb17X.PO4.0.2O2.TdepJohn2014.0.4PO4.SPIN','AP.445eb17X.PO4.1.0O2.TdepJohn2014.0.2PO4.SPIN']
#exps = ['AP.445eb12X.PO4.1.0O2.TdepJohn2014.1.0PO4.SPIN','AP.445eb12X.PO4.0.4O2.TdepJohn2014.1.0PO4.SPIN','AP.445eb12X.PO4.0.2O2.TdepJohn2014.0.4PO4.SPIN','AP.445eb12X.PO4.1.0O2.TdepJohn2014.0.2PO4.SPIN']
#exps = ['AP.445eb24X.PO4.0.6O2.TdepJohn2014.0.6PO4.SPIN','AP.445eb17X.PO4.0.6O2.TdepJohn2014.0.6PO4.SPIN','AP.445eb5X.PO4.0.6O2.TdepJohn2014.0.6PO4.SPIN']

#indir= '/archive/crct/al1966po/Phanerozoic_GENIE/HIRNANTIAN/genie_output/ensemble'
#exps = ['AP.445eb12X.PO4.1.0O2.TdepJohn2014.1.0PO4.SPIN']

#indir= '/archive/crct/al1966po/Phanerozoic_GENIE/HIRNANTIAN/genie_output'
#exps = ['AP.445eb12X.PO4.100kyr.SPIN']

varIDs = np.array([1, 2, 5])

# if only 1 series and 2 vars ...
coaxes = 'y' # do we plot both curves on a single graph?

timemin = 0
timemax =20000

do_legend = 'n'
save_fig = 'y'
##########################


# LIST OF VARIABLES
#  0  ::  global ocean area (Mkm2)
#  1  ::  global mean O2 (mol kg-1)
#  2  ::  benthic O2 ($\mu$mol kg-1)
#  3  ::  global POC flux (mol yr-1)
#  4  ::  mean global ventilation age (yr)
#  5  ::  benthic ventilation age (yr)
#  6  ::  surface air temperature (degrees C)
#  7  ::  NC - eco2D_Size_Mean -- Geometric Mean of Cell Diameter
#  8  ::  NC -- eco2D_Size_Frac_Micro_Chl -- Micro chlorophyll biomass
#  9  ::  NC -- eco2D_Size_Frac_Nano_Chl -- Nano chlorophyll biomass
# 10  ::  NC -- eco2D_Size_Frac_Pico_Chl -- Pico chlorophyll biomass
# 11  ::  global min overturning (Sv)
# 12  ::  global max overturning (Sv)
# 13  ::  global sea-ice area (Mm2)
# 14  ::  global sea-ice volume (Mm3)
# 15  ::  mean sea-ice thickness (m)

# nothing to change below this line

# number of series and vars to plot
nexps = np.shape(exps)[0]
nvars = np.shape(varIDs)[0]

if nexps > 1 or nvars != 2 or coaxes != 'y':
    print('More than 1 exp or += than 2 vars, disabling coaxes')
    coaxes = 'n'

if coaxes == 'y':
    print('Co-axis requested; legend turned off')
    do_legend = 'n'

# using standard python frontend instead of the web browser
mpl.use('TkAgg')
# ignore future warnings
warnings.filterwarnings("ignore", category=FutureWarning)

plot_font_size = 20
mpl.rc('font', size=plot_font_size)


var_counter = 0
# looping over variables and plotting one figure with several exps by variable
for varID in varIDs[:]:

    # standard values
    factor = 1
    offset = 0
    geniesubdir = 'biogem'

    exec(open('/archive/crct/al1966po/Phanerozoic_GENIE/PHANERO/genie_analysis/resvar_plotting_params.py').read())

    # reformatting for plotting purposes if varname is toooooo loooong
    if len(varname) > 20:
        varname2plot = "\n".join(textwrap.wrap(varname,22))

    print('================= Variable: ' + varname + ' =================')

    lines = []

    if (coaxes != 'y' or var_counter != 1):
        fig = plt.figure(figsize=(15.,7.))
        ax = fig.add_subplot(111)
        ax = fig.gca()

    exp_counter = 0
    for exp in exps:

        print('---- Experiment: ' + exp + ' ----')

        infile = indir + '/' + exp + '/' + geniesubdir + '/' + txtfile

        # reading table headers to determine...
        table_headers = pd.read_csv(infile,delimiter="/", header=0, engine='python',nrows=0)
        # number of columns
        ncols = np.shape(table_headers)[1]
        # and using ncols to read content of the table
        table_content = pd.read_csv(infile, names=list(range(ncols)),engine='python',skiprows=1, delim_whitespace=True).to_numpy() # varID1 > (450, 6)

        # extracting time slice of interest
        time = table_content[:,0]
        T = np.argwhere((timemin <= time) & (time <= timemax)) # table_content[T,0] = 9999.5 ok !]
        # ... and associated value
        val = table_content[T,col]
        vals2plot = val * factor + offset
        time2plot = time[T]

        if (coaxes == 'y'): # if coaxis requested
            if var_counter == 0:
                vals2plot_1 = vals2plot
                varname_1 = varname2plot
                varname2save_1 = varname2save
            else:
                vals2plot_2 = vals2plot
                varname_2 = varname2plot
                varname2save_2 = varname2save
                varname2save = varname2save_1 + '_and_' + varname2save_2

        exp_counter += 1

        # if first pass with coaxes later
        if coaxes == 'n': # if std, we do not give the color
            lines += ax.plot(time2plot,vals2plot,'-', linewidth=1.5, label=exp,zorder=4)
            ax.set_ylabel(varname2plot)
            ax.grid(); ax.grid(color='grey', linestyle='--', linewidth=0.5, dashes=(0.6, 1))
            ax.set_xlabel('Model run time (yr)')
            ax.set_xlim((timemin-5, timemax+5))
        elif (coaxes == 'y' and var_counter != 1): # if first pass of coaxes, col = black
            lines += ax.plot(time2plot,vals2plot,'-', linewidth=1.5, label=exp,zorder=4, color='k')
            ax.set_ylabel(varname2plot)
            ax.grid(); ax.grid(color='grey', linestyle='--', linewidth=0.5, dashes=(0.6, 1))
            ax.set_xlabel('Model run time (yr)')
            ax.set_xlim((timemin-5, timemax+5))
        else:  # if second pass with coaxis
            ax2 = ax.twinx()
            color = 'tab:blue'
            lines += ax2.plot(time2plot,vals2plot,'-', linewidth=1.5, label=exp,color=color)
            ax2.set_ylabel(varname2plot, color=color)
            #plt.tight_layout()
            ax2.tick_params(axis='y', labelcolor=color)
            #ax2.tick_params(axis='x', labelsize=plot_font_size*0.8)
            #ax2.tick_params(axis='y', labelsize=plot_font_size*0.8)

        if exp_counter == nexps:
            if do_legend == 'y':
                labels = [l.get_label() for l in lines]
                ax.legend(lines, labels, loc='center left',bbox_to_anchor=(1.04,0.5), fontsize='x-small')
            plt.subplots_adjust(right=0.7)
            plt.tight_layout()

    var_counter += 1

    if (coaxes != 'y' or var_counter != 1):
        if save_fig == 'y':
            suffix='.pdf';
            fname = 'res__' + varname2save + '_' + exp + suffix
            plt.savefig(fname,format='pdf')
            print('        Saving to file: ' + fname)

