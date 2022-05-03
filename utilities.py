# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:45:22 2021

@author: joeglbe
"""

def colours (seq):
    """Loops through a STR and adds binary colour to each character"""
    binary_colours={
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
        }
    
    tmpStr= ""
    for nuc in seq:
        if nuc in binary_colours:
            tmpStr+= binary_colours[nuc] +nuc
        else:
            tmpStr+= binary_colours['reset'] +nuc
    return tmpStr + '\033[0;0m'

print(colours("ATGCU"))
            