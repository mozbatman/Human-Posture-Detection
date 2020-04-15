# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import ast

veriler = pd.read_csv("../veriler_val.csv")

img = mpimg.imread('../dataset/val2017/'+veriler["file_name"][3])
print(veriler["file_name"][3])

bbox = veriler["bbox"][3]
bbox = ast.literal_eval(bbox)
print(bbox)

kp = veriler["keypoints"][3]
kp = ast.literal_eval(kp)
print(kp)



## BBOX - RECTANGLE Draw
fig,ax = plt.subplots(1)
ax.imshow(img)
rect = patches.Rectangle((bbox[0],bbox[1]),bbox[2],bbox[3],linewidth=1,edgecolor='r',facecolor='none')
ax.add_patch(rect)


## KEYPOİNTS Draw
for i in range(0,len(kp),3):
    if kp[i+2] > 1:
        plt.plot(kp[i], kp[i+1],'o',markersize=4)
        





plt.show()

