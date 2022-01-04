#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# def Conexion(vertex_table, edge_table):
    
#     conexion = {}
#     for dest in vertex_table['key']:
#         destination = edge_table.loc[edge_table['destination'] == dest]
#         conexion[dest] = {origin:destination.loc[destination['origin'] == origin, ['larger_radius']].values[0][0]/
#                           sum(edge_table.loc[edge_table['origin'] == origin]['larger_radius'])
#                             for origin in destination['origin']}
#     return conexion


def Conexion(vertex_table, edge_table):
    
    conexion = {}
    for dest in vertex_table['key']:
        destination = edge_table.loc[edge_table['destination'] == dest]
        conexion[dest] = {origin:(destination.loc[destination['origin'] == origin, ['larger_radius']].values[0][0])**2/
                          sum((edge_table.loc[edge_table['origin'] == origin]['larger_radius'])**2)
                            for origin in destination['origin']}
    return conexion