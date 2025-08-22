# ===============================================================
# File:            SU2MeshReader.py
# Project:         Blade Tip Surface Identification
# Description:     SU2 Mesh Reader class
#
# Author:          Joshua A. Kelly
# Insititution:    Univeristy of Liverpool
# Date Created:    01/08/2025 (DD/MM/YYYY)
# Python Version:  3.10.13
#
# Dependencies:    numpy
#
# ===============================================================

import numpy as np
from utils.io import readData

class SU2Mesh:
    def __init__(self, fname):
        self.mesh_fname = fname
        self.mesh_data = self.readMesh()
        self.blade_data = self.getBladeData()
        self.blade_elems = self.getBladeElemArray(self.blade_data[2:])
        pass
    
    def readMesh(self):
        with open(self.mesh_fname, "r") as f:
            mesh_lines = f.readlines()
        return mesh_lines


    def getBladeData(self):
        blade_found = False
        marker_tag_found = False
        for i, line in enumerate(self.mesh_data):
            if blade_found and not marker_tag_found:
                if "MARKER_TAG" in line:
                    print(f"and ends on line {i-1}")
                    marker_tag_found = True
                    data_end = i
            if "BLADE" in line:
                blade_found = True
                print(f"Blade defintion starts on line {i}")
                data_start = i
        blade_data = self.mesh_data[data_start:data_end]
        return blade_data
    
    def getBladeElemArray(self, blade_elems):
        elems_list = list()
        for elem in blade_elems:
            line = elem.split("\t")
            line = [int(i) for i in line]
            if line[0] == 5:
                # Add an extra 0 index so array shape is consistent
                # Do this as we don't care about the triangular elements as they are not on the edge of the tip
                line.append(0)
            elems_list.append(line[1:])
        elems_array = np.array(elems_list)
        return elems_array
    
    def getAdjacentIndices(self, search_indices):
        adjacent_indices = list()
        for elem in self.blade_elems:
            for i in elem:
                if i in search_indices:
                    # An element contains an index on the tip -> whole element is on the tip
                    for j in elem:
                        if j not in adjacent_indices and j not in search_indices and j != 0:
                            # Elements not already present in adjacent indices and search lists
                            adjacent_indices.append(j)
                    break # Added all indices in element to list
        return adjacent_indices

        




