#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:39:25 2019

@author: ron

This is a script is made for generating Nodes and Boundaries, and to set
proper neighbuors for each of them, given a d dimensional space.

"""

from node import Node, Boundary
from utills import get_seqs
import numpy as np



class Grid(object):
    '''
    a d dimensional solution grid. The 2d space bounderies are given in the 
    list "lims". The number of grid Nodes in each dimension are given in the 
    list N.
    
    lims - nested list of floats with dimensions dX2
    N    - list of integers with length d
    '''
    
    def __init__(self, lims, N):
        
        self.d = len(N)
        self.lims = lims
        self.N = N
        self.dx = [ (lims[i][1] - lims[i][0]) / N[i] for i in range(self.d)]
        
        # a list of coordinates for each dimension:
        self.coords = []
        for i in range(self.d):
            self.coords.append([self.lims[i][0] +
                     self.dx[i]*(j+0.5) for j in range(self.N[i])])
        
        # a long series of all coordinates and a series of indexes:
        # (this can be usefull for when iterating over dimensions)
        self.coords_seq = get_seqs(self.coords)  
        ind = [range(i) for i in self.N]
        self.coords_index = get_seqs(ind)  
        
        
    def get_coord_index(self, coord):
        '''
        returns the indexes (dimension indexes) of a coordinate 
        '''
        return self.coords_index[ self.coords_seq.index( list(coord) ) ]
    
    
    def get_coord_number(self, coord):
        '''
        returns the single index of a coordinate 
        '''
        return self.coords_seq.index( list(coord) )
        
        
    def make_nodes(self):
        '''
        will generate a list of nodes, a list of boundaries and asociate each
        with it's neighbours.
        '''
        self.nodes = []
        for c in self.coords_seq:
            self.nodes.append(  Node( np.array(c) , np.array(self.dx) )  )
        
        # connect neighbuoring Nodes and set boundaries:
        self.boundaries = []
        for nd in self.nodes:
            ind = self.get_coord_index( nd.x )
            neighbuors = []
            
            # find the 2d neighbuors (or boundaries)
            for i in range(len(ind)):
                neighbuors.append([])
                
                # left neighbuor
                if ind[i]==0:
                    # add boundary:
                    x0 = np.zeros(self.d)
                    x0[i] = x0[i]-self.dx[i]
                    c = nd.x + x0
                    b = Boundary( c, np.array(self.dx) )
                    self.boundaries.append(b)
                    neighbuors[-1].append(b)
                    
                else:    
                    x0 = np.zeros(self.d)
                    x0[i] = x0[i]-1
                    ind_im1 = list(np.array(ind) + x0)
                    nd_im1 = self.nodes[self.coords_index.index(ind_im1)]
                    neighbuors[-1].append(nd_im1)
                
                # right neighbuor:
                if ind[i]==self.N[i]-1:
                    # add boundary:
                    x1 = np.zeros(self.d)
                    x1[i] = x1[i]+self.dx[i]
                    c = nd.x + x1
                    b = Boundary( c, np.array(self.dx) )
                    self.boundaries.append(b)
                    neighbuors[-1].append(b)
                    
                else:    
                    x1 = np.zeros(self.d)
                    x1[i] = x1[i]+1
                    ind_ip1 = list(np.array(ind) + x1)
                    nd_ip1 = self.nodes[self.coords_index.index(ind_ip1)]
                    neighbuors[-1].append(nd_ip1)
            
            nd.set_neighbuors(neighbuors)



#lims = [[0.0, 1.0]]
#N =  [10]
#g = Grid( lims, N)
#g.make_nodes()








