# -*-coding:GBK-*-
import os
def IsSubString(SubStrList,Str):
 ''''' 
 #判断字符串Str是否包含序列SubStrList中的每一个子字符串 
 #>>>SubStrList=['F','EMS','txt'] 
 #>>>Str='F06925EMS91.txt' 
 #>>>IsSubString(SubStrList,Str)#return True (or False) 
 '''
 flag=True
 for substr in SubStrList:
  if not(substr in Str):
   flag=False
 return flag

def GetFileList(FindPath,FlagStr=[]):
 ''''' 
 #获取目录中指定的文件名 
 #>>>FlagStr=['F','EMS','txt'] #要求文件名称中包含这些字符 
 #>>>FileList=GetFileList(FindPath,FlagStr) # 
 '''
 import os
 FileList=[]
 FileNames=os.listdir(FindPath)
 if (len(FileNames)>0):
  for fn in FileNames:
   if (len(FlagStr)>0):
    #返回指定类型的文件名
    if (IsSubString(FlagStr,fn)):
     fullfilename=os.path.join(FindPath,fn)
     FileList.append(fullfilename)
   else:
    #默认直接返回所有文件名
    fullfilename=os.path.join(FindPath,fn)
    FileList.append(fullfilename)
 #对文件名排序
 if (len(FileList)>0):
  FileList.sort()
 return FileList
#以上函数功能为寻找指定目录下的文件的，为百度上面寻找得到的

# i = open("shuwa2017/week/homework/skytravelor.txt").read()
# for document in GetFileList(u'shuwa2017/week/homework/dic/主题/', 'txt'):
#     file_now = open(document)
#     file_read = file_now.readline().strip()
#     x = 0
#     while file_read:
#         if file_read in i:
#              x = x +1
#         file_read = file_now.readline().strip()
#     print x

def handsome(u):
    sky = open("shuwa2017/week/homework/skytravelor.txt").read()  #shuwa2017/week/homework/skytravelor.txt为太空旅客评论
    for document in GetFileList(u, 'txt'):
        file_now = open(document)
        file_read = file_now.readline().strip()
        x = 0
        while file_read:
            if file_read in sky:
                x = x + 1
            file_read = file_now.readline().strip()
        print x

handsome(u'shuwa2017/week/homework/dic/主题/')  #u'shuwa2017/week/homework/dic/主题/'为关键字txt文本目录地址