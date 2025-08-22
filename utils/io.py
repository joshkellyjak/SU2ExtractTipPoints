# ===============================================================
# File:            io.py
# Project:         Blade Tip Surface Identification
# Description:     I/O utilities
#
# Author:          Joshua A. Kelly
# Insititution:    Univeristy of Liverpool
# Date Created:    01/08/2025 (DD/MM/YYYY)
# Python Version:  3.10.13
# 
# Dependencies:    os, numpy, configparser
#
# ===============================================================

import os
import numpy as np
import configparser
from core.point import Point


class Config:
    def __init__(self, config_loc):
        self.config_loc = os.path.basename(config_loc)
        self.wdir = os.path.dirname(config_loc)
        cwd = os.getcwd()
        os.chdir(cwd + '/' + self.wdir)
        self.readConfig()
        pass

    def readConfig(self):
        if not os.path.exists(self.config_loc):
            raise FileNotFoundError(f"Config file not found: {self.config_loc}")
        
        self.config = configparser.ConfigParser()
        self.config.read(self.config_loc)

        config_dict = {}
        for section in self.config.sections():
            config_dict[section] = {}
            for key, value in self.config[section].items():
                try:
                    config_dict[section][key] = eval(value)
                except:
                    config_dict[section][key] = value

        self.IN = config_dict
            
def readData(fname):
    with open(fname, "r") as f:
        data = np.genfromtxt(f, delimiter="\t")
    return data

def readPointData(data, transform):
    point_data = list()
    for row in data:
        point = Point(row[0], row[1], row[2], row[3], transform)
        point_data.append(point)
    return point_data

def writeCombinedMoveSurface(fname, point_data):
    with open(fname, 'w') as f:
        for point in point_data:
            line = f"{point.index}\t{point.x}\t{point.y}\t{point.z}\n"
            f.write(line)
