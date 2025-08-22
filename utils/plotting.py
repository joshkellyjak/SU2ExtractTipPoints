# ===============================================================
# File:            plotting.py
# Project:         Blade Tip Surface Identification
# Description:     Plotting utilities
#
# Author:          Joshua A. Kelly
# Insititution:    Univeristy of Liverpool
# Date Created:    01/08/2025 (DD/MM/YYYY)
# Python Version:  3.10.13
#
# Dependencies:    matplotlib
#
# ===============================================================

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotPoints(points):
    """
    Takes input of point data and plots 3D cartesian field
    """
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for p in points:
        ax.scatter(p.x, p.y, p.z, color='black', s=1)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

def plotCylPoints(points):
    """
    Takes input of point data and plots in 2D meridional plane
    """
    fig = plt.figure()
    ax = fig.add_subplot()
    for p in points:
        ax.scatter(p.r, p.z, color='black', s=1)
    ax.set_xlabel("R")
    ax.set_ylabel("Z")



