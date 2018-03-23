#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 01:56:26 2018

@author: apple
"""
import json

with open('/Users/apple/Desktop/Code/python_crawl/getCourseraPlan/item.json', 'r') as f:
    data = f.readlines()
    for d in data:
        j_d = json.loads(d)
        j_v = list(j_d.values())
        with open('/Users/apple/Desktop/Code/python_crawl/getCourseraPlan/data.csv', 'ab+') as f2:
            line = ','.join(j_v) + '\n'
            f2.write(line.encode('utf-8'))