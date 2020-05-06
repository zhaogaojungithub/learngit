#! /usr/bin/python3
import pickle
data1 = {'a':[1,2.0,3,4+6j],'b':('string','int'),'c':None}
selfref_list = [1,2,3]
selfref_list.append(selfref_list)
output = open('./file/data.pkl','wb')
pickle.dump(data1,output)
pickle.dump(selfref_list,output,2)
output.close()
