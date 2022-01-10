'''
    移除与source中 document.sentiment相同的句子，
    mr7_1
    nltk

'''
import os

def read(data,path):
    f=open(path,'r')
    for string in f:
        data.append(string)
    f.close()
def write(data,path):
    f=open(path,'w')
    for string in data:
        f.write(string)
    f.close()
if __name__ == '__main__':
    index=1
    count=2000
    while index<=count:
        data_s=[]
        data_os=[]
        data_f=[]
        s_path = "E:/MT_SA/data/input/mr7_1/nltk/s%s.txt" %index
        if os.path.exists(s_path):
            os_path="E:/MT_SA/data/output/mr7_1/nltk/os%s.txt" %index
            read(data_os,os_path)
            read(data_s,s_path)
            document_sentiment=data_os[len(data_os)-1].split("negative=")[0].split("document_sentiment=")[1].strip()  #存储document的sentiment
            f_path="E:/MT_SA/data/input/mr7_1/nltk/f%s.txt" %index

            for i in range(len(data_s)):
                sentiment=data_os[i].split("negative=")[0].split("sentiment=")[1].strip()
                if sentiment !=document_sentiment:
                    data_f.append(data_s[i])
            write(data_f,f_path)
        index+=1

    print("ok")








