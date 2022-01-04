#!/usr/bin/env python
# coding: utf-8

# In[2]:


from GraphFunc.PageRankFunction import PageRank
from GraphFunc.ConexionFunction import Conexion
from GraphFunc.ZeoDataframeFunction import ZeoDataframe
from GraphFunc.EdgeFileFunction import EdgeFile
from GraphFunc.SupercellFunction import Supercell
from GraphFunc.ShortestPathFunction import ShortestPath
import pickle
import numpy as np
import pandas as pd
import pymatgen 
from pymatgen.core.structure import Structure
from optparse import OptionParser
import os
import random

# In[ ]:


if __name__ == '__main__':

    optparser = OptionParser()
    # Supercell
    optparser.add_option('--name_mat', dest='name_mat', help='string name', default='EDI')
    optparser.add_option('--cif_file', dest='cif_file', help='CSV filename', default='CifFiles/EDI.cif')
    optparser.add_option('--lattice_mult', dest='lattice_mult', help='lattice_mult (int)', default=4, type='int')
    optparser.add_option('--supercell_file', dest='supercell_file', help='CSV filename', default='SupercellFiles/SuperEDI4.cif')
    # nt2 to Dataframe
    optparser.add_option('--nt2_file', dest='nt2_file', help='CSV filename', default='Nt2Files/SuperEDI4.nt2')
    # Bounds text file
    optparser.add_option('--bound_file', dest='bound_file', help='CSV filename', 
                         default='BoundFiles/BoundEDI4.text')
    # Pagerank algorithm
    optparser.add_option('--iteration', dest='iteration', help='Iteration (int)', default=100, type='int')
    
    
    
    (options, args) = optparser.parse_args()
    
    name_mat = options.name_mat
    cif_path = 'CifFiles/' + str(name_mat) + '.cif'

    lattice_mult = options.lattice_mult
    supercell_path = 'SupercellFiles/Super' + str(name_mat) + str(lattice_mult) + '.cif'
    #supercell_path = options.supercell_file
    nt2_path = 'SupercellFiles/Super' + str(name_mat) + str(lattice_mult) + '.nt2'
    #nt2_path = options.nt2_file
    bound_path = 'BoundFiles/Bound' + str(name_mat) + str(lattice_mult) + '.text'
    #bound_path = options.bound_file
    
    iteration = options.iteration
    
    result_dir = 'result'
    fname = cif_path.split('/')[-1].split('.')[0] + str(lattice_mult)
    
 
    
# Supercell
n = lattice_mult

lattice_vector = [n,n,n]

cell_dim = Supercell(cif_path, lattice_vector, supercell_path)

# nt2 file

# Convert nt2 file into Dataframe objects
multiplier = np.array([1,1,1]) #6.4
box = np.array([cell_dim[0], cell_dim[1], cell_dim[2]])

edge_table, vertex_table = ZeoDataframe(nt2_path, multiplier, box)

# Create a file that describe conexions between nodes
path_edge_file = EdgeFile(bound_path, edge_table)

# Dictionary used to calulatate the proporcion among the conexion in every node
conexion = Conexion(vertex_table, edge_table)

# Pagerank algorithm 
# return an ax with the selected node located 
info, sum_nodes = PageRank(path_edge_file, conexion, iteration)

# Shortest's Path Algorithm
most_connected_node = np.argsort(info)[-1] 
start = random.choice(list(range(len(vertex_table))))

node_path = ShortestPath(most_connected_node, start, vertex_table, edge_table)


# print('Shortest Path:')
# print(path[0])
# print('Distances Shortest Path:')
# print(path[1])
# print('Sum:')
# print(sum(path[1]))

#pagerank_fname = '_PageRank.txt'
#path = os.path.join(result_dir, fname)
#os.makedirs(path, exist_ok=True)
#print(os.path.join(path, fname + pagerank_fname))
#print(np.array(node_path[0]))
#np.savetxt(os.path.join(path, fname + pagerank_fname), np.array([path[0]]), newline=" ") #, fmt='%.3f'

