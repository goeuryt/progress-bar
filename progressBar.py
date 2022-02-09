#! /usr/bin/python
# -*-coding:Utf-8 -*

# ----------------------------------------------------------------------------- #
#
# Implementation of a progress bar to use within loops
#
# ----------------------------------------------------------------------------- #
#
# Author: Inconnu - Modified by Thomas Goeury
# Date: 17 / 03 / 2015
# Language: Python 2.7
# 
# ----------------------------------------------------------------------------- #

import sys 

class ProgressBar:
    '''
    Progress Bar    
    '''
    def __init__ (self, valmax, maxbar, title, output='stdout'):
        self.valmax = 1 if valmax == 0 else valmax
        self.maxbar = 200 if maxbar > 200 else maxbar
        self.title  = title
        self.val    = 0
        self.output = output
    
    def update(self):
        perc  = round((float(self.val) / float(self.valmax)) * 100)
        scale = 100.0 / float(self.maxbar)
        bar   = int(perc / scale)
        out   = '\r %20s [%s%s] %3d %%' % (self.title, '=' * bar, ' ' * (self.maxbar - bar), perc)
        if self.output == 'stdout':
            sys.stdout.write(out)
            sys.stdout.flush()
        elif self.output == 'stderr':
            sys.stderr.write(out)
            sys.stderr.flush()
        else:
            print('ERROR: Unknown output')
            exit()
        self.val += 1


# EOF
