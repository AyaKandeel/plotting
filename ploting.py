# matplotlib - 2D and 3D plotting in Python"
# This line configures matplotlib to show figures embedded in the notebook
# instead of opening a new window for each figure. More about that later
# If you are using an old version of IPython, try using '%pylab inline' instead
## Introduction
import matplotlib.pyplot as plt
import numpy as np
## MATLAB-like API
from pylab import *
### Example
x = np.linspace(0, 5, 10)
y = x ** 2
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('equation')
show()
subplot(1,2,1)
plot(x, y, 'r--')
subplot(1,2,2)
plot(y, x, 'g*-')
## The matplotlib object-oriented API"
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes
# main figure
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')
# insert
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title')
fig, axes = plt.subplots()
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
fig, axes = plt.subplots(nrows=1, ncols=2)
for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
fig, axes = plt.subplots(nrows=1, ncols=2)
for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
fig.tight_layout()
fig = plt.figure(figsize=(8,4), dpi=100)
fig, axes = plt.subplots(figsize=(12,3))
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
### Saving figures
fig.savefig('filename.png')
fig.savefig('filename.png', dpi=200)
#### What formats are available and which ones should be used for best quality
### Legends, labels and titles
ax.set_title('title')
ax.set_xlabel(x)
ax.set_ylabel(y)
ax.legend(["curve1","curve2","curve3"])
ax.plot(x, x**2, label='curve1')
ax.plot(x, x**3, label='curve2')
ax.legend()
ax.legend(loc=0) # let matplotlib decide the optimal location
ax.legend(loc=1) # upper right corner
ax.legend(loc=2) # upper left corner
ax.legend(loc=3) # lower left corner
ax.legend(loc=4) # lower right corner
# .. many more options are available
fig, ax = plt.subplots()
ax.plot(x, x**2, label='y = x**2')
ax.plot(x, x**3, label='y = x**3')
ax.legend(loc=2); # upper left corner
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')
### Formatting text: LaTeX, fontsize, font family
fig, ax = plt.subplots()
ax.plot(x, x**2, label=r'$y = alpha^2$')
ax.plot(x, x**3, label=r'$y = alpha^3$')
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$alpha$', fontsize=18)
ax.set_ylabel(r'$y$', fontsize=18)
ax.set_title('title')
# Update the matplotlib configuration parameters
matplotlib.rcParams.update({'font.size': 18, 'font.family': 'serif'})
fig, ax = plt.subplots()
ax.plot(x, x**2, label=r'$y = alpha^2$')
ax.plot(x, x**3, label=r'$y = alpha^3$')
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('title')
# Update the matplotlib configuration parameters
matplotlib.rcParams.update({'font.size': 18, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})
fig, ax = plt.subplots()
ax.plot(x, x**2, label=r'$y = alpha^2$')
ax.plot(x, x**3, label=r'$y = alpha^3$')
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('title')
matplotlib.rcParams.update({'font.size': 18, 'text.usetex': True})
fig, ax = plt.subplots()
ax.plot(x, x**2, label=r'$y = alpha^2$')
ax.plot(x, x**3, label=r'$y = alpha^3$')
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('title')
# restore
matplotlib.rcParams.update({'font.size': 12, 'font.family': 'sans', 'text.usetex': False})
### Setting colors, linewidths, linetypes
#### Colors
# MATLAB style line color and style 
ax.plot(x, x**2, 'b.-') # blue line with dots
ax.plot(x, x**3, 'g--') # green dashed line
fig, ax = plt.subplots()
ax.plot(x, x+1, color='red', alpha=0.5) # half-transparant red
ax.plot(x, x+2, color='#1155dd')        # RGB hex code for a bluish color
ax.plot(x, x+3, color='#15cc55')        # RGB hex code for a greenish color
#### Line and marker styles
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(x, x+1, color='blue', linewidth=0.25)
ax.plot(x, x+2, color='blue', linewidth=0.50)
ax.plot(x, x+3, color='blue', linewidth=1.00)
ax.plot(x, x+4, color='blue', linewidth=2.00)
# possible linestype options ‘-‘, ‘--’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color='red', lw=2, linestyle='-')
ax.plot(x, x+6, color='red', lw=2, ls='-.')
ax.plot(x, x+7, color='red', lw=2, ls=':')
# custom dash
line, = ax.plot(x, x+8, color='black', lw=1.50)
line.set_dashes([5, 10, 15, 10]) # format: line length, space length, 
# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color='green', lw=2, ls='--', marker='+')
ax.plot(x, x+10, color='green', lw=2, ls='--', marker='o')
ax.plot(x, x+11, color='green', lw=2, ls='--', marker='s')
ax.plot(x, x+12, color='green', lw=2, ls='--', marker='1')
# marker size and color
ax.plot(x, x+13, color='purple', lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color='purple', lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color='purple', lw=1, ls='-', marker='o', markersize=8, markerfacecolor='red')
ax.plot(x, x+16, color='purple', lw=1, ls='-', marker='s', markersize=8, markerfacecolor='yellow', markeredgewidth=2, markeredgecolor='blue')
### Control over axis appearance
#### Plot range  
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].plot(x, x**2, x, x**3)
axes[0].set_title('default axes ranges')
axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title('tight axes')
axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title('custom axes range')
#### Logarithmic scale  
fig, axes = plt.subplots(1, 2, figsize=(10,4))
axes[0].plot(x, x**2, x, np.exp(x))
axes[0].set_title('Normal scale')
axes[1].plot(x, x**2, x, np.exp(x))
axes[1].set_yscale('log')
axes[1].set_title('Logarithmic scale (y)') 
### Placement of ticks and custom tick labels
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, x**2, x, x**3, lw=2)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels([r'$alpha$', r'$beta$', r'$gamma$', r'$delta$', r'$epsilon$'], fontsize=18)
yticks = [0, 50, 100, 150]
ax.set_yticks(yticks)
ax.set_yticklabels(['$%.1f$' % y for y in yticks], fontsize=18) # use LaTeX formatted labels
#### Scientific notation
fig, ax = plt.subplots(1, 1)
ax.plot(x, x**2, x, np.exp(x))
ax.set_title('scientific notation')
ax.set_yticks([0, 50, 100, 150])
from matplotlib import ticker
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
ax.yaxis.set_major_formatter(formatter)
### Axis number and axis label spacing   
# distance between x and y axis and the numbers on the axes
matplotlib.rcParams['xtick.major.pad'] = 5
matplotlib.rcParams['ytick.major.pad'] = 5
fig, ax = plt.subplots(1, 1)
ax.plot(x, x**2, x, np.exp(x))
ax.set_yticks([0, 50, 100, 150])
ax.set_title('label and axis spacing')
# padding between axis label and axis numbers
ax.xaxis.labelpad = 5
ax.yaxis.labelpad = 5
ax.set_xlabel('x')
ax.set_ylabel('y')
# restore defaults
matplotlib.rcParams['xtick.major.pad'] = 3
matplotlib.rcParams['ytick.major.pad'] = 3
#### Axis position adjustments
fig, ax = plt.subplots(1, 1)
ax.plot(x, x**2, x, np.exp(x))
ax.set_yticks([0, 50, 100, 150])
ax.set_title('title')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.subplots_adjust(left=0.15, right=.9, bottom=0.1, top=0.9)
### Axis grid
fig, axes = plt.subplots(1, 2, figsize=(10,3))
# default grid appearance
axes[0].plot(x, x**2, x, x**3, lw=2)
axes[0].grid(True)
# custom grid appearance
axes[1].plot(x, x**2, x, x**3, lw=2)
axes[1].grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
### Axis spines
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    