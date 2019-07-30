from shapely.ops import cascaded_union, polygonize
from scipy.spatial import Delaunay
import numpy as np
import math
import shapely.geometry as geometry
import matplotlib.pyplot as plt


#Source: https://sgillies.net/2012/10/13/the-fading-shape-of-alpha.html
class ConcaveHull():
    def __init__(self,points):
        self.points = points

    def calc_hull(self,alpha = 1.5):
        if len(self.points) < 4:
            return geometry.MultiPoint(list(self.points)).convex_hull

        points = self.points
        delaunay = Delaunay(points)
        print(type(delaunay))
        edges = set()
        edge_points = []
        # loop over triangles:
        # ia, ib, ic = indices of corner points of each triangle
        for ia, ib, ic in delaunay.vertices:
            tri_point_1 = points[ia]
            tri_point_2 = points[ib]
            tri_point_3 = points[ic]

            #side lengths
            len_a = math.sqrt((tri_point_1[0]-tri_point_2[0])**2 + (tri_point_1[1]-tri_point_2[1])**2)
            len_b = math.sqrt((tri_point_2[0]-tri_point_3[0])**2 + (tri_point_2[1]-tri_point_3[1])**2)
            len_c = math.sqrt((tri_point_3[0]-tri_point_1[0])**2 + (tri_point_3[1]-tri_point_1[1])**2)

            # Semiperimeter of triangle
            s = (len_a + len_b + len_c)/2.0

            # Area of triangle by Heron's formula
            area = math.sqrt(s*(s-len_a)*(s-len_b)*(s-len_c))
            circum_r = len_a*len_b*len_c/(4.0*area)


            def add_edge(edges, edge_points, points, i, j):
                if (i,j) in edges or (j,i) in edges:
                    return
                edges.add((i,j))
                edge_points.append(points[[i,j]])

            # Radius filter
            if circum_r < 1.0/alpha:
                add_edge(edges, edge_points, points, ia, ib)
                add_edge(edges, edge_points, points, ib, ic)
                add_edge(edges, edge_points, points, ic, ia)

        m = geometry.MultiLineString(edge_points)
        triangles = list(polygonize(m))
        return cascaded_union(triangles)
