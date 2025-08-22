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
        if transform:
            self.transformCoordinates()
        pass

    def getRadialDistance(self):
        # Gets radial distance from origin
        return self.r
    
    def setMCoordinate(self, m):
        self.m = m
        pass
    
    def transformCoordinates(self, theta=-10*np.pi/180):
        """
        Here we transform coordinates as to avoid singularities encountered
        when considering trigonometric operations at 90 degrees
        The transformed coordinates are given by chi and eta, z is conserved
        """
        self.chi = self.z*np.cos(theta) - self.r*np.sin(theta)
        self.eta = self.z*np.sin(theta) + self.r*np.cos(theta)
        pass

def getPoint(index, points):
    """
    Finds the point with given index in a list of points
    """
    for point in points:
        if point.index == index:
            return point
    raise Exception("The given index does not match any point in the list!")


def getCoords(points):
    """
    This returns the cartesian coordinates for a point, this is used when coordinate
    values are needed
    """
    return np.array([[p.x, p.y, p.z] for p in points])

def getCylindricalCoords(points):
    return np.array([[p.r, p.theta, p.z] for p in points])

def getTransformXY(x, y, alfa):
    a = x*np.cos(alfa) - y*np.sin(alfa)
    b = x*np.sin(alfa) + y*np.cos(alfa)
    return a, b

def getRemovedSharedPoints(points_a, points_b):
    """
    Given a list of points A, remove the points that are also present in list B and return
    """
    a_index = [p.index for p in points_a]
    b_index = [p.index for p in points_b]

    shared_index = list(set(a_index) & set(b_index))

    return [getPoint(index, points_a) for index in a_index if index not in shared_index]

def getRemovedDuplicateVals(points, bar=False):
    """
    Returns a list of points where there are no duplicate values of a given variable
    """
    
    seen = set()
    unique_coords = list()
    removed_indices = list()

    if bar:
        progress = ProgressBar(len(points))

    for i, coord in getEnumRZData(points):
        if bar:
            progress.update(int(i))
            
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
        yield index, [round(point.r, 8), round(point.z, 8)]
    
def buildPointDictionary(points):
    """
    Builds a dictionary of points: cart. coord
    """
    point_dict = defaultdict(Point)
    for p in points:
        point_dict[int(p.index)] = p
    return point_dict