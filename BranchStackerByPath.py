'''
Created on 24/06/2015

@author: EJArizaR
'''
from BranchStacker import BranchStacker

class BranchStackerByPath(BranchStacker):

    NAME_KEY = "name"

    def __init__(self, data, rootID):
        self._rootID = rootID
        self._data = data        
        self._stack = []
        self._setOfLinks = set()
        self._setOfBranches = set()
        self._populateStack()
        
    @property
    def stack(self):
        return self._stack
    
    def _populateStack(self):
        for dataEntry in self._data:
            self._setOfLinks.add(dataEntry[self.NAME_KEY])
            self._setOfLinks = self._setOfLinks.union(dataEntry[self.LINKS_KEY])
            
        for link in self._setOfLinks:
            self._appendSublevelsFromLink(link)
        
        for element in self._setOfBranches:
            self._stack.append({self.ID_KEY:element[0], self.PARENT_KEY:element[1], self.WEIGHT_KEY:element[2], self.NAME_KEY:element[3]})
            
        self._stack.sort(key=lambda x:x[self.WEIGHT_KEY])
 
    def _appendSublevelsFromLink(self, dataEntry):        
        pathLevels = self._getPathLevels(dataEntry)
        if len(pathLevels)>0 and pathLevels[0] == self._rootID:
            pathLevels.insert(0, self.ROOT)
            subSetOfBranches = {(self._getNodeID(pathLevels, i), self._getNodeID(pathLevels, i - 1), i, pathLevels[i]) for i in range(1, len(pathLevels))}        
            self._setOfBranches = self._setOfBranches.union(subSetOfBranches)

    def _createBranch(self, nodeID, parentID, weight, nodeName):
        return {self.ID_KEY:nodeID, self.PARENT_KEY:parentID, self.WEIGHT_KEY:weight, self.NAME_KEY:nodeName}
 
    def _getPathLevels(self, link):
        if self._rootID not in link:
            return []
        else:
            linkWithoutRoot = link.replace(self._rootID, "")
            urlWithoutscheme = linkWithoutRoot.split("://")[-1]
            pathSublevels = urlWithoutscheme.split("/")
            if pathSublevels[0] == "":
                pathSublevels.pop(0)
            pathSublevels.insert(0,self._rootID)    
            return pathSublevels   
    
    def _getNodeID(self, pathLevels, indexOfNode):
        if indexOfNode == 0:
            return self.ROOT
        return "/".join(pathLevels[1:indexOfNode + 1])
                        