#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Tatiana Lenskaia, 2024
"""
import core_methods as cm




path = "/Users/tl/fas_initial/"
fListName = "flist.txt"


path_out = "/Users/tl/faa/"

t = cm.GetListFromFile(path+fListName)

print(t, len(t))

d = {}

for fname in t:
    f = open(path+fname, "r")
    lab = fname.rsplit(".",1)[0]
    fOut = open(path_out+lab+".faa","w")
    c = 0
    for line in f:
        if line[0] == ">":
            c += 1
            #print(line)
            line = ">"+lab+" ### "+line[1:]
        fOut.write(line)
        
    f.close()
    fOut.close()
    
    if lab not in d:
        d[lab] = c

fOutName = "stat.txt"

fOut = open(path+fOutName,"w")
for it in t:
    lab = it.rsplit(".",1)[0]
    print(lab, str(d[lab]), file = fOut, sep = "\t")
fOut.close()

print(d)
