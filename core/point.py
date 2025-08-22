# ===============================================================
# File:            point.py
# Project:         Blade Tip Surface Identification
# Description:     Point class
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
from collections import defaultdict
from functools import partial

class Point:
    def __init__(self, _index, _x, _y, _z, transform):
        self.index = int(_index)
        self.x = _x
        self.y = _y
        self.z = _z
        self.r = np.sqrt(self.x**2 + self.y**2)
        self.theta = np.arctan2(self.y, self.x)
        pass

def getPoint(index, points):
    """
    Finds the point with given index in a list of points
    """
    for point in points:
        if point.index == index:
            return point
    raise Exception("The given index does not match any point in the list!")

def getRemovedSharedPoints(points_a, points_b):
    """
    Given a list of points A, remove the points that are also present in list B and return
    """
    a_index = [p.index for p in points_a]
    b_index = [p.index for p in points_b]

    shared_index = list(set(a_index) & set(b_index))

    return [getPoint(index, points_a) for index in a_index if index not in shared_index]

def getRemovedDuplicateVals(points):
    """
    Returns a list of points where there are no duplicate values of a given variable
    """
    
    seen = set()
    unique_coords = list()
    removed_indices = list()

    for i, coord in getEnumRZData(points):
        if coord[0] not in seen:
            unique_coords.append(coord)
            seen.add(coord[0])
        else:
            removed_indices.append(i)
    
    idx_filtered = [p.index for p in points if p.index not in removed_indices]

    return [getPoint(index, points) for index in idx_filtered]

def getEnumRZData(points):
    for point in points:
        index = point.index
        yield index, [point.r, point.z]
    
def buildPointDictionary(points):
    """
    Builds a dictionary of points: cart. coord
    """
    point_dict = defaultdict(Point)
    for p in points:
        point_dict[int(p.index)] = p
    return point_dict