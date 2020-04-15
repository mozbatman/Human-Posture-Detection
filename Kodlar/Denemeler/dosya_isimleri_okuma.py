import os 

su_an = os.getcwd()
print(su_an) 

veriler = os.listdir("D:/Programlama/PostureDetections/dataset/annotations")

f = open("isimler.txt","w+")
for i in veriler:
    print(i)
    f.write(i+"\n")

f.close()
