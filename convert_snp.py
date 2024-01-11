#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 01:29:11 2024

@author: Gloria
"""

# Read dbSNP data
dbSNP = {}
with open("dbSNP_chrom_pos_rsID.txt") as file:
    for line in file:
        chrom, pos, rsid = line.strip().split()
        dbSNP[(chrom, pos)] = rsid

# Read and update BIM file
with open("ascherio_EUR_modified.bim") as bim, open("ascherio_EUR_rsID.bim", "w") as out:
    for line in bim:
        parts = line.strip().split()
        chrom_pos = parts[1].split(':')
        rsid = dbSNP.get((chrom_pos[0], chrom_pos[1]), parts[1])
        parts[1] = rsid
        out.write('\t'.join(parts) + '\n')
