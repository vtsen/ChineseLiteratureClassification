# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 18:08:34 2018

@author: Zhen
"""

import os
from paragraph import Paragraph as PG

def make_paragraphs(raw_data_path, decorated_data_path, urn, aux_info):
    text, info = "", ""         # from urn
    aux = decorate(info ,aux_info)
    paragraphs = text.split('\n')
    for p in paragraphs:
        pg = PG(p, info)
        pg.set_aux_info(aux)
        pg.save_to_file(decorated_data_path)

def decorate(info, aux_info):
    return dict()       # aux dict

def get_aux_info(aux_path):
    pass

if __name__ == "__main__":
    aux_path = ""
    raw_data_path = ""
    decorated_data_path = ""
    
    urns = []   # from raw_data_path
    aux_info = get_aux_info(aux_path)
    
    for urn in urns:
        make_paragraphs(raw_data_path, decorated_data_path, urn, aux_info)
    