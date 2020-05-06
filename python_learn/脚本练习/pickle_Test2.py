#! /usr/bin/python3
import pickle
print("从文件反序列化数据.......")
f = open("./file/data.pkl","rb")
data1 = pickle.load(f)
print(data1)
data2 = pickle.load(f)
print(data2)
data3 = pickle.load(f)
print(data)
f.close()
