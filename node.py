#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 14:02:29 2019

@author: ron


This script holds the "Node" object - the essential element in the discritized 
domain, and the "Boundary" object which is a special type of node that has only
one neighbuor with which there is an interaction. 
"""



class Node(object):
    '''
    initially each node has a position "x" and dimensions "dx" - both arrays
    of D dimentsions.
    
    use set_param to add physical parameters to each node
    '''
    def __init__(self, x, dx):
        
        self.d = len(x)   # number of dimensions of phase space
        self.x = x        # location in phase space
        self.dx = dx      # size length of the node in phase space
    
    
    def set_param(self, param_name, value):
        
        setattr(self, param_name, value)


    def set_neighbuors(self, neighbuors):
        '''
        In each direction of phase space, the node needs to have two borders --
        for example, in the direction i<=d, the neighbuors of the node will be
        node@d[i-1], node@d[i+1].
        Therefore, to specify the neighbuors of each node the input neighbuors
        is a list of length d, such that each element is a list of 2 nodes, the
        first at d[i-1] and the other at d[i+1]
        '''
        if type(neighbuors) != list: 
            raise TypeError('input need to be a nested list dX2')
        
        if len(neighbuors) != self.d: 
            raise ValueError('input need to be a nested list dX2')
            
        for itm in neighbuors:
            if len(itm) != 2:
                raise ValueError('input need to be a nested list dX2')
        
        self.neighbuors = neighbuors
        
        
        
        
        
        
class Boundary(object):
    '''
    Has a position "x" and dimensions "dx" - both arrays
    of D dimentsions. In a simulation, a Boundary cell will be positioned
    outside of the domain, and one of it's borders will coiside with a boudery
    of the doimain (through which the interaction with a single Node provides 
    setting of the Boundary condition).
    
    use set_param to add physical parameters.
    '''
    def __init__(self, x, dx):
        
        self.d = len(x)   # number of dimensions of phase space
        self.x = x        # location in phase space
        self.dx = dx      # size length of the node in phase space
    
    
    def set_param(self, param_name, value):
        
        setattr(self, param_name, value)


    def set_neighbuor(self, neighbuor):
        '''
        A Boundary can have only one neighbuor (although a node can have
        as much as d Boundary neighbuors). The neighbuor has to be a Node.
        '''
        if type(neighbuor) != Node: 
            raise TypeError('input has to be a Node object')
            
        self.neighbuor = neighbuor
        
    