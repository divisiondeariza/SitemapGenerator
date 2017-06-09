'''
Created on 25/06/2015

@author: EJArizaR
'''

class LinksFormatter(object):
    def __init__(self):
        '''
        Constructor
        '''

    
    def formatLink(self, link):
        if link[-1] == "/":
            return link[0:-1]
        return link
    
    
        