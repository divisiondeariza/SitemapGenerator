'''
Created on 24/06/2015

@author: EJArizaR
'''

class BranchStacker(object):
    ROOT = "Root"
    ID_KEY = "id"
    PARENT_KEY = "parent"
    WEIGHT_KEY = "weight"
    LINKS_KEY = "children"


    def __init__(self, params):
        '''
        Constructor
        '''
        
    @property
    def stack(self):
        raise NotImplementedError("Subclasses should implement this!")
        