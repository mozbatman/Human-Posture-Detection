import json 
import pandas as pd

with open("D:/Programlama/PostureDetections/dataset/annotations/person_keypoints_train2017.json") as f:
    data = json.load(f)
    
with open("D:/Programlama/PostureDetections/dataset/annotations/instances_train2017.json") as f:
    data2 = json.load(f)
    
df = pd.DataFrame(columns=["file_name","coco_url","bbox","keypoints","segmentation",'width','height'])

ann = data["annotations"]
ann2 = data2["annotations"]
images = data2["images"]

for i in ann2:
    if i["category_id"] == 1:
        for j in images:
            if j["id"] == i["image_id"]:
                for k in ann:
                    if k["image_id"] == i["image_id"]:
                        df = df.append([{'file_name':j["file_name"],'coco_url':j["coco_url"],
                                         'bbox':i["bbox"],'keypoints':k["keypoints"],
                                         'segmentation':k["segmentation"],'width':j["width"],'height':j["height"]}],ignore_index=True)
                        # f = open("isimler.txt","w+")
                        # f.write(j["file_name"]+","+j["coco_url"]+","+i["bbox"]+","+k["keypoints"]+","+k["segmantation"]+"\n")
                        # f.close()
                        break
                break
            
            
            
# df = df.drop_duplicates(subset=['file_name'])
# df.to_csv("veriler.csv",encoding='utf-8', index= False)
                
df = df.drop_duplicates(subset=['file_name'])
df.to_csv("veriler_train.csv",encoding='utf-8', index= False)            
            