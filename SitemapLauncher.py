'''
Created on 1/07/2015

@author: ejarizar
'''
import json
from BranchStackerByPath import BranchStackerByPath
from BranchStackerByChildren import BranchStackerByChildren
from TreeAssembler import TreeAssembler
import os
from ScraperDANE.SpiderLauncher import SpiderLauncher

class SitemapLauncher(object):


    GENERATE_LINKS_FLAG = "--generate-links"
    LINKSFILE = "<LINKSFILE>"
    SITEMAPFILE = "<SITEMAPFILE>"
    MIN_CLICK_FLAG = "--by-min-clicks"
    ROOT_KEY = "<ROOT>"

    def __init__(self, args):
        self.args = args
        

    def run(self):
        
        if self.args[self.GENERATE_LINKS_FLAG]:
            spiderLauncher = SpiderLauncher()
            filepath = os.path.abspath(self.args[self.LINKSFILE])
            if os.path.isfile(filepath):
                os.remove(filepath)
            spiderLauncher.run(filepath)
        
        with open(self.args[self.LINKSFILE]) as linksfile:
            data = json.load(linksfile)

        treeAssembler = TreeAssembler()  
        if not self.args[self.MIN_CLICK_FLAG]:
            stack = BranchStackerByPath(data, self.args[self.ROOT_KEY]).stack #"www.dane.gov.co"
        else:
            stack = BranchStackerByChildren(data, self.args[self.ROOT_KEY]).stack #"http://www.dane.gov.co/"            
        tree  = treeAssembler.generateTree(stack, self.args[self.ROOT_KEY])
        
        with open(self.args[self.SITEMAPFILE], "wb") as fp:
            json.dump(tree, fp, indent=4)
            pass
        