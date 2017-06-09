'''
Created on 22/06/2015

@author: EJArizaR
'''

class TreeAssembler(object):
    ID_KEY = "id"
    PARENT_KEY = "parent"
    WEIGHT_KEY = "weight"
    LINKS_KEY = "children"
    NAME_KEY = "name"


    def __init__(self):
        '''
        Constructor
        '''

    def generateTree(self, stack, rootID = None):
        print rootID
        if rootID == None:
            root = next(branch for branch in stack if branch[self.WEIGHT_KEY] == 1)       
        else:
            root = next(branch for branch in stack if branch[self.ID_KEY] == rootID)
        tree = self._generateBranch(stack, root)
        return tree
    

    def _generateBranch(self, stack, root):
        node = {}
        links = []
       
        if self.NAME_KEY in root.keys(): 
            node[self.NAME_KEY] = root[self.NAME_KEY]
        else:
            node[self.NAME_KEY] = root[self.ID_KEY]
        for child in [branch for branch in stack if branch[self.PARENT_KEY] == root[self.ID_KEY]]:
            links.append(self._generateBranch(stack, child))
        if len(links)>0:
            node[self.LINKS_KEY] = links
        return node            

    
        