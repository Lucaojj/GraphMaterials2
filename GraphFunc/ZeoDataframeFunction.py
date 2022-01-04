#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[8]:



def ZeoDataframe(path_nt2, multiplier, box):
    
    import pandas as pd
    import numpy as np
    x_1 = 70
    
    # All Data
    path_to_file = path_nt2
    alldata = pd.read_csv(path_to_file)

    # Transform the output from Zeo++ to Dataframe structure

    # Box's size took it from the cif file



    vertex_table = pd.DataFrame({'coord_x':[], 'coord_y':[], 'coord_z':[],
                                 'min_dist_atom':[], 'key':[]})
    edge_table = pd.DataFrame({'origin':[], 'destination':[]})

    with open(path_to_file) as f:
        line = ' '

        while line:
            line = f.readline()

            if line == 'Vertex table:\n':
                while line:

                    line = f.readline()
                    if line == '\n':
                        break
                    line_list = line.split()
                    key = line_list[0]
                    coord_x = float(line_list[1])*multiplier[0]
                    coord_y = float(line_list[2])*multiplier[1]
                    coord_z = float(line_list[3])*multiplier[2]
                    min_dist_atom = float(line_list[4])
                    vertex_table = vertex_table.append({'coord_x':coord_x, 'coord_y':coord_y, 'coord_z':coord_z,
                                                        'min_dist_atom':min_dist_atom, 'key':key},ignore_index = True)
            elif line == 'Edge table:\n':

                while line:

                    line = f.readline()
                    if line == '':
                        break
                    line_list = line.split()
                    origin = line_list[0]
                    destination = line_list[2]
                    larger_radius = float(line_list[3])
                    x_sim = int(line_list[4])
                    y_sim = int(line_list[5])
                    z_sim = int(line_list[6])
                    if sum([abs(x_sim), abs(y_sim), abs(z_sim)]) == 0:
                        edge_table = edge_table.append({'origin':origin, 'destination': destination, 'x_sim':x_sim,
                                                        'y_sim':y_sim, 'z_sim':z_sim,'larger_radius':larger_radius},
                                                       ignore_index = True)
                        
                    elif x_sim == 8:
                        edge_table = edge_table.append({'origin':origin,'destination':str(int(destination) + x_1),
                                                        'x_sim':x_sim,
                                                        'y_sim':y_sim, 'z_sim':z_sim,
                                                        'larger_radius':larger_radius},ignore_index = True)
                        edge_table = edge_table.append({'origin':str(int(destination) + x_1),'destination':origin,
                                                        'x_sim':x_sim,
                                                        'y_sim':y_sim, 'z_sim':z_sim,
                                                        'larger_radius':larger_radius},ignore_index = True)
                        
                        vertex_table = vertex_table.append({
                            'coord_x':vertex_table.loc[vertex_table['key']  == str(destination), ['coord_x']].values[0][0] + box[0],                               
                            'coord_y':vertex_table.loc[vertex_table['key']  == str(destination),['coord_y']].values[0][0],                                 'coord_z':vertex_table.loc[vertex_table['key']  == str(destination), ['coord_z']].values[0][0],
                            'min_dist_atom':vertex_table.loc[vertex_table['key']  == str(destination),['min_dist_atom']].values[0][0],
                            'key':str(int(destination) + x_1)},ignore_index = True)
                        #print('change')
                    else:
                        pass
    dim = 3



    # Function for the calculation of distances between axes
    def distance(origin, destination, vertex_table, box):

        dim = 3

        p1 = vertex_table.loc[vertex_table['key'] == origin, ['coord_x', 'coord_y', 'coord_z']].values[0]
        p2 = vertex_table.loc[vertex_table['key'] == destination, ['coord_x', 'coord_y', 'coord_z']].values[0]

        dist_3d = np.zeros((dim))
        for j in range(dim):
            dist = abs(p2[j]-p1[j])
            if dist > box[j] * 0.5:
                dist = abs(box[j] - dist)
            dist_3d[j] = dist


        return np.sqrt(np.sum(np.power(dist_3d, 2)))

    # Calculation of the edge's distances
    edge_dist = edge_table.apply(lambda x: distance(x[0], x[1], vertex_table, box), axis=1)
    edge_table = edge_table.assign(edge_dist=edge_dist)
    
    print('DataFrame DONE')
    return edge_table, vertex_table


# In[9]:


# edge_table, vertex_table = ZeoDataframe('/home/lucasperea/Documents/1.A_Dijkstra/Voronoi/EDI.nt2',
#                                          np.array([6.9, 6.9, 6.83]), np.array([6.9260, 6.9260, 6.4100]))


# In[ ]:





# In[ ]:




