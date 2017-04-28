# -*-coding:GBK-*-
import os
def IsSubString(SubStrList,Str):
 ''''' 
 #�ж��ַ���Str�Ƿ��������SubStrList�е�ÿһ�����ַ��� 
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
 #��ȡĿ¼��ָ�����ļ��� 
 #>>>FlagStr=['F','EMS','txt'] #Ҫ���ļ������а�����Щ�ַ� 
 #>>>FileList=GetFileList(FindPath,FlagStr) # 
 '''
 import os
 FileList=[]
 FileNames=os.listdir(FindPath)
 if (len(FileNames)>0):
  for fn in FileNames:
   if (len(FlagStr)>0):
    #����ָ�����͵��ļ���
    if (IsSubString(FlagStr,fn)):
     fullfilename=os.path.join(FindPath,fn)
     FileList.append(fullfilename)
   else:
    #Ĭ��ֱ�ӷ��������ļ���
    fullfilename=os.path.join(FindPath,fn)
    FileList.append(fullfilename)
 #���ļ�������
 if (len(FileList)>0):
  FileList.sort()
 return FileList
#���Ϻ�������ΪѰ��ָ��Ŀ¼�µ��ļ��ģ�Ϊ�ٶ�����Ѱ�ҵõ���

# i = open("shuwa2017/week/homework/skytravelor.txt").read()
# for document in GetFileList(u'shuwa2017/week/homework/dic/����/', 'txt'):
#     file_now = open(document)
#     file_read = file_now.readline().strip()
#     x = 0
#     while file_read:
#         if file_read in i:
#              x = x +1
#         file_read = file_now.readline().strip()
#     print x

def handsome(u):
    sky = open("shuwa2017/week/homework/skytravelor.txt").read()  #shuwa2017/week/homework/skytravelor.txtΪ̫���ÿ�����
    for document in GetFileList(u, 'txt'):
        file_now = open(document)
        file_read = file_now.readline().strip()
        x = 0
        while file_read:
            if file_read in sky:
                x = x + 1
            file_read = file_now.readline().strip()
        print x

handsome(u'shuwa2017/week/homework/dic/����/')  #u'shuwa2017/week/homework/dic/����/'Ϊ�ؼ���txt�ı�Ŀ¼��ַ