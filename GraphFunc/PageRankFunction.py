#!/usr/bin/env python
# coding: utf-8

# In[62]:


import os
import pickle
import numpy as np


# In[136]:


# with open('../../EDI/EDI_Conexion', 'rb') as handle:
#     conexion = pickle.load(handle)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[200]:


# PageRank('/home/lucasperea/Documents/1.A_Dijkstra/EDI/EDI_Text.txt', conexion, 100)


# In[16]:


def PageRank(path_edge_file, conexion, iteration):
    
    import numpy as np
    
    class Graph:
        def __init__(self):
            self.nodes = []

        def contains(self, name):
            for node in self.nodes:
                if(node.name == name):
                    return True
            return False

        # Return the node with the name, create and return new node if not found
        def find(self, name):
            if(not self.contains(name)):
                new_node = Node(name)
                self.nodes.append(new_node)
                return new_node
            else:
                return next(node for node in self.nodes if node.name == name)

        def add_edge(self, parent, child):
            parent_node = self.find(parent)
            child_node = self.find(child)

            parent_node.link_child(child_node)
            child_node.link_parent(parent_node)

#        def display(self):
#            for node in self.nodes:
#               print(f'{node.name} links to {[child.name for child in node.children]}')

        def sort_nodes(self):
            self.nodes.sort(key=lambda node: int(node.name))

#         def normalize_pagerank(self):
#             pagerank_sum = sum(node.pagerank for node in self.nodes)

#             for node in self.nodes:
#                 node.pagerank /= pagerank_sum

        def get_pagerank_list(self):
            pagerank_list = np.asarray([node.pagerank for node in self.nodes], dtype='float32')
            return pagerank_list


    class Node:
        def __init__(self, name):
            self.name = name
            self.children = []
            self.parents = []
            self.pagerank = 1

        def link_child(self, new_child):
            for child in self.children:
                if(child.name == new_child.name):
                    return None
            self.children.append(new_child)

        def link_parent(self, new_parent):
            for parent in self.parents:
                if(parent.name == new_parent.name):
                    return None
            self.parents.append(new_parent)

        def update_pagerank(self, conexion):
            in_neighbors = self.parents #self.parents
            pagerank_sum = sum(node.pagerank*conexion[self.name][node.name]
                               for node in in_neighbors)
            self.pagerank = pagerank_sum




    def init_graph(fname):
        with open(fname) as f:
            lines = f.readlines()

        graph = Graph()

        for line in lines:
            [parent, child] = line.strip().split(',')
            graph.add_edge(parent, child)

        graph.sort_nodes()

        return graph

    def PageRankInt(graph, iteration, conexion):
        for i in range(iteration):
            last = PageRank_one_iter(graph, conexion)
        return(last)

    def PageRank_one_iter(graph, conexion):
        node_list = graph.nodes
        for node in node_list:
            node.update_pagerank(conexion)
#         graph.normalize_pagerank()
        return(graph.get_pagerank_list())
    
    graph = init_graph(path_edge_file)
    info = PageRankInt(graph, iteration, conexion)
    
    print('Number of total nodes: {}'.format(len(info)),
          '\n\nBest connected node: {}'.format(np.argmax(info)),
          '\n\nvalues for best connected node: {}, worst connected node: {}'.format('%.10f'%(np.max(info)),
                                                                                    '%.10f'%(np.min(info))),
          '\n\nSum of values of all nodes: {}'.format('%.10f'%(sum(info))))

    print('PageRank DONE')
    return info, sum(node.pagerank for node in graph.nodes)


# In[ ]:





# In[ ]:





# In[146]:






# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




