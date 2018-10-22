# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 18:02:28 2018

@author: Zhen
"""

import os
import json
import ctext as ct

from utils import urn_to_str

def read_data_from_json(raw_data_path, urn):
    filename = urn_to_str(urn) + ".json"
    with open(os.path.join(raw_data_path, filename), 'r') as fp:
        data = json.load(fp)
    return data

def fetch_data_from_ctext(raw_data_path, urn):
    data = ct.gettextasobject(urn)
    filename = urn_to_str(urn) + ".json"
    with open(os.path.join(raw_data_path, filename), 'w') as fp:
        json.dump(data, fp)

def is_urn_stored(raw_data_path, urn):
    filename = urn_to_str(urn) + ".json"
    return filename in os.listdir(raw_data_path)

if __name__ == "__main__":
    #ct.s
    #eta
    #pike
    #y("d
    #emo")
    urns = ["ctp:analects/xue-er", "ctp:analects/wei-zheng",
            "ctp:analects/ba-yi"]
    raw_data_path = "raw"
    for urn in urns:
        if not is_urn_stored(raw_data_path, urn):
            print(urn)
            fetch_data_from_ctext(raw_data_path, urn)
         
    for urn in urns:
        data = read_data_from_json(raw_data_path, urn)
        print(urn)
        print(data)