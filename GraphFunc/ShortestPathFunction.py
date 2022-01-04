#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[30]:


# path = ShortestPath(7, 6, vertex_table, edge_table)


# In[34]:


def ShortestPath(most_connected_node, start, vertex_table, edge_table):

    import random
    import pandas as pd
    import numpy as np
    from queue import PriorityQueue
    from numpy import inf
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
#     get_ipython().run_line_magic('matplotlib', 'notebook')
    class Graph:

        def __init__(self, num_of_vertices, dist_mat):
            self.v = num_of_vertices
            self.edges = dist_mat
            self.visited = []

        def add_edge(self, u, v, weight):
            self.edges[u][v] = weight
            self.edges[v][u] = weight

        def dijkstra(self, start_vertex, target, parents):

            # Dictionary with keys = vertices and values = weights of the vertices (set as infinity at the start)
            D = {}
            D = {v:float('inf') for v in range(self.v)}
            D[start_vertex] = 0

            pq = PriorityQueue()
            pq.put((0, start_vertex))

            while not pq.empty():
                (dist, current_vertex) = pq.get()
                if current_vertex == target:
                    print('Target vertex: ' + str(target) + ' reached')
                    break
                else:

                    self.visited.append(current_vertex)


                    # Loop for every vertex of the net
                    for neighbor in range(self.v):
                        if self.edges[current_vertex][neighbor] != -1:
                            distance = self.edges[current_vertex][neighbor]
                            if neighbor not in self.visited:
                                old_cost = D[neighbor]
                                new_cost = D[current_vertex] + distance
                                if new_cost < old_cost:
                                    pq.put((new_cost, neighbor))
                                    D[neighbor] = new_cost
                                    parents[str(neighbor)] = current_vertex

            return D, parents

        def backpedal(self, start_vertex, target, searchResult):

            node = str(target)

            backpath = [node]

            path = []

            while node != str(start_vertex):

                backpath.append(str(searchResult[node]))

                node = str(searchResult[node])

            for i in range(len(backpath)):

                path.append(backpath[-i - 1])

            return path 
    
    # initialization of the Graph and distance Matrix

    list_nodes = [int(num) for num in list(vertex_table['key'])]

    N = len(list_nodes)
    dist_mat = np.ones((N, N))*-1

    # Dictionary to translate from nodes to his position in vertex_table

    trans_pos_nod = {}
    for i in range(N):
        trans_pos_nod[str(i)] = int(vertex_table['key'][i])

    trans_nod_pos = {}
    for i in range(len(vertex_table['key'])):
        trans_nod_pos[vertex_table['key'][i]] = i


    radius_mat = np.ones(dist_mat.shape)

    # Loop to create conexion between the nodes
    for i in range(len(edge_table)):
        origin = edge_table.iloc[i,0]
        destination = edge_table.iloc[i,1]

        origin_index = vertex_table.loc[vertex_table['key'] == origin].index.values[0]
        destination_index = vertex_table.loc[vertex_table['key'] == destination].index.values[0]


        dist_mat[origin_index, destination_index] = edge_table.iloc[i, 6]
        radius_mat[origin_index, destination_index] = edge_table.iloc[i, 2]
        
    g = Graph(N, dist_mat)

    parents = {}


    D, P = g.dijkstra(start, most_connected_node, parents)
    
    path = g.backpedal(str(start), str(most_connected_node), P)
    
    distance_path = []
    for i in range(len(path)-1):
        
        distance_path.append(dist_mat[int(path[i]), int(path[i+1])])

    node_path = []

    for part in path:
        node_path.append(trans_pos_nod[part])

        
    print('Start index: {}'.format(start))
    print('Start node: {}'.format(trans_pos_nod[str(start)]))
    print('Final index: {}'.format(most_connected_node))
    print('Finalt node: {}'.format(trans_pos_nod[str(most_connected_node)]))
    print()
    print('Path with matrix indexs: {}'.format(path))
    print()
    print('Path with nodes names: {}'.format(node_path))
    print()
    print('Distances between nodes in the path: {}'.format(distance_path))    
    print()
    print('Total Distance: {}'.format(sum(distance_path))) 
    print()
    print()
    print()
    # Matrix with the cartesians coordinates of all the nodes in the system
    dim = 3
    pos_mat = np.zeros((N, dim))

    for i in range(N):
        pos_mat[i,:] = vertex_table.loc[vertex_table.index == i, ['coord_x', 'coord_y', 'coord_z']].values[0]
        
        
    fig = plt.figure(figsize=(8,8))

    ax = fig.add_subplot(111, projection='3d')

    # Plot the most connected node
    ax.scatter(vertex_table.loc[vertex_table.index == most_connected_node, ['coord_x']].values[0][0],
               vertex_table.loc[vertex_table.index == most_connected_node, ['coord_y']].values[0][0],
               vertex_table.loc[vertex_table.index == most_connected_node, ['coord_z']].values[0][0],
               s=100, c='red') 

    # Plot of lines connecting all the path's nodes
    for i in range(len(node_path)-1):

        ax.plot([pos_mat[int(path[i])][0], pos_mat[int(path[i+1])][0]], 
                [pos_mat[int(path[i])][1], pos_mat[int(path[i+1])][1]],
                zs=[pos_mat[int(path[i])][2], pos_mat[int(path[i+1])][2]], linewidth=4)

    # Plot al nodes 
    x_ax = pos_mat[:,0]
    y_ax = pos_mat[:,1]
    z_ax = pos_mat[:,2]

    ax.scatter(x_ax,y_ax,z_ax, s=10, c='black')

    plt.show()
    
    return node_path, distance_path


# In[ ]:





# In[ ]:





# In[3]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




