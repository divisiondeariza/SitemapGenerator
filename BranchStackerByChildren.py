'''
Created on 19/06/2015

@author: EJArizaR
'''
from BranchStacker import BranchStacker


class BranchStackerByChildren(BranchStacker):
    
    NAME_KEY = "name"

    def __init__(self, data, rootID):
        self._rootID = rootID
        self._data = data
        self._stack = []
        self._alreadyAddedNodesIDs = [rootID]        
        self._populateStack()

    @property
    def stack(self):
        return self._stack

    def _populateStack(self):
        self._addToStackRecursively(self._rootID, self.ROOT)
            
    def _addToStackRecursively(self, nodeID, parentName, weight = 1):
        self._stack.append({self.ID_KEY:nodeID, self.PARENT_KEY:parentName, self.WEIGHT_KEY:weight})
        if nodeID in [node[self.NAME_KEY] for node in self._data]:
            self._addChildsToStack(nodeID, weight)

    def _addChildsToStack(self, nodeID, nodeWeight):
        node = next(element for element in self._data if element[self.NAME_KEY] == nodeID)
        for child in [link for link in node[self.LINKS_KEY] if link not in self._alreadyAddedNodesIDs]:
            self._alreadyAddedNodesIDs = self._alreadyAddedNodesIDs + node[self.LINKS_KEY]
            self._addToStackRecursively(child, nodeID, nodeWeight + 1)        