# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 18:17:58 2018

@author: Zhen
"""

import os
import pandas as pd

class Paragraph(object):
    '''
    
    '''
    
    def __init__(self, text, info):
        self.text = text
        self.info = info        #TODO: break down to dynasty, title, and toptitle
        self.aux = dict()
        
    def set_aux_info(self, aux_info):
        self.aux = aux_info
    
    def save_to_file(self, filename):
        pass
    
    def read_from_file(self, filename):
        pass
    
    def get_text(self):
        return self.text