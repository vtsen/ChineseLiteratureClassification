# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 18:02:28 2018

@author: Zhen
"""

import os
import ctext as ct

def fetch_data_from_ctext(urn):
    pass

def is_urn_stored(raw_data_path, urn):
    return True

if __name__ == "__main__":
    urns = []
    raw_data_path = ""
    for urn in urns:
        if not is_urn_stored(raw_data_path, urn):
            fetch_data_from_ctext(urn)