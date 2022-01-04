#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[48]:




def Supercell(path_cif, lattice_vector, path_supercell):
    
    import pymatgen
    from pymatgen.core.structure import Structure
    from pymatgen.io.cif import CifWriter
    
    struct = Structure.from_file(path_cif)
    struct.make_supercell(lattice_vector)
    
    CifWriter(struct).write_file(path_supercell)
    print('Supercell DONE')
    return struct.lattice.abc


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




