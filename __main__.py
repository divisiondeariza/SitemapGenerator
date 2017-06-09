'''
Created on 30/06/2015

@author: EJArizaR

usage:
    SitemapGenerator [-p|-m]  <LINKSFILE> <SITEMAPFILE> <ROOT>
    SitemapGenerator [-p|-m]  -g <LINKSFILE> <SITEMAPFILE> <ROOT>
    SitemapGenerator -h

options:   
    -h, --help             Show this screen
    -p, --by-path          Generates the map by directory paths in urls 
                           [default]
    -m, --by-min-clicks    Generates the map by minimum (suboptimal) clicks 
                           needed for achieve the url from root
    -g, --generate-links   Generates the <LINKSFILE> running the spider 
                           before
    -r, --root             Root of the sitemap
'''

from docopt import docopt
from SitemapLauncher import SitemapLauncher

args = docopt(__doc__, version='Sitemap Generator')
launcher = SitemapLauncher(args)
launcher.run()
