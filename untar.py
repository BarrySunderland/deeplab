# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:12:01 2020

@author: BarryS
"""


import os, sys, tarfile

tar = tarfile.open(sys.argv[1], 'r:gz')
tar.extractall()
print('Done.')
#except:
#    name = os.path.basename(sys.argv[0])
#    print(name[:name.rfind('.')], '<filename>')