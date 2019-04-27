#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 16:53:40 2019

@author: ron
"""

def get_seqs(lst):
    '''
    returns a set of all combinations of values from a nested list.
    '''
    if len(lst)>1:
        k = get_seqs(lst[1:])
        new_lst = []
        for i in lst[0]:
            for j in k:
                new_lst.append([i] + j)
        
        return new_lst
    
    else:
        return [[i] for i in lst[0] ]
    