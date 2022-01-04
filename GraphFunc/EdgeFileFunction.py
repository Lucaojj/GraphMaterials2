#!/usr/bin/env python
# coding: utf-8

# In[1]:


def EdgeFile(path_edge_file, edge_table):

    import pandas as pd
    with open(path_edge_file, 'w') as f:
        for i in range(len(edge_table)):
            text = ''
            for l in edge_table.loc[edge_table.index == i, ['origin', 'destination']].values[0].tolist():
                line = l + ','
                text += line 
            f.write(text.strip(',')  + '\n')
    print('Edge File DONE')        
    return path_edge_file


# In[ ]:




