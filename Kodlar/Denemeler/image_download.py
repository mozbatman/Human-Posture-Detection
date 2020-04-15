# -*- coding: utf-8 -*-

import urllib.request


def download(url, file_path, file_name):
    full_path = file_path + file_name
    urllib.request.urlretrieve(url, full_path)
    
veriler = pd.read_csv("../veriler_val.csv")

for i in len(veriler.count):
    download(veriler["coco_url"], "../datasets/val2017/", veriler["file_name"])
    
