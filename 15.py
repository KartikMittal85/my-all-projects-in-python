from pymongo import MongoClient
ct=MongoClient('localhost',27017)
myd=ct['mymongo']
myc=myd['staff']
ex=input('enter city') 
x=myc.count_documents({'city':ex})
print(x)