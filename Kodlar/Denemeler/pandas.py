# -*- coding: utf-8 -*-

import pandas as pd


df = pd.DataFrame(columns=["file_name","coco_url","bbox","keypoints","segmantation"])
df = df.append([{'file_name':12,'coco_url':1}],ignore_index=True)
