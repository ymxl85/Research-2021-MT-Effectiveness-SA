'''
    缩写

'''
import csv

def mutant(sentence,set):
    flag=0
    f_sentence=""
    for j in range(len(set[0])):
        tagword1 = set[0][j] + " "
        tagword2 = " " + set[0][j] + " "
        if sentence.find(tagword1) != -1:
            if sentence.index(tagword1) == 0:
                newword = set[1][j] + " "
                f_sentence = sentence.replace(tagword1, newword, 1)
                flag = 1
                break
        if sentence.find(tagword2) != -1:
            if sentence.index(tagword2) != -1:
                newword = " " + set[1][j] + " "
                f_sentence = sentence.replace(tagword2, newword, 1)
                flag = 1
                break

    if flag==0:
        for j in range(len(set[1])):
            tagword1=set[1][j]+" "
            tagword2=" "+set[1][j]+" "
            if sentence.find(tagword1) != -1:
                if sentence.index(tagword1)==0:
                    newword=set[0][j]+" "
                    f_sentence=sentence.replace(tagword1,newword,1)
                    flag=1
                    break
            if sentence.find(tagword2)!=-1:
                if sentence.index(tagword2) != -1:
                    newword=" "+set[0][j]+" "
                    f_sentence=sentence.replace(tagword2,newword,1)
                    flag=1
                    break

    return f_sentence

def getDict(path):
    with open(path, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        column1  = [row['_tion'] for row in reader]
    csvfile.close()
    with open(path, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        column2 = [row['Prototype'] for row in reader]
    csvfile.close()
    return column1,column2

def write(data,path):
    f=open(path,'w')
    for string in data:
        f.write(string)
    f.close()

def read(data,path):
    f=open(path,'r')
    for string in f:
        data.append(string)
    f.close()

if __name__ == '__main__':
    path="E:/MT_SA/MRelation/mr1/list1.csv"
    count=2000
    index=1
    num=0
    data=getDict(path)
    path1="E:/MT_SA/data1/input/log_11.txt"  # 用来存储生成的follow-up文件
    f3=open(path1,'a')
    while index<=count:
        data_ex=[]
        data_f=[]
        data_s=[]
        ex_path = "E:/MT_SA/data/input/source1/s%s.txt" %index
        f_path = "E:/MT_SA/data1/input/mr11/f%s.txt" %index
        s_path = "E:/MT_SA/data1/input/mr11/s%s.txt" %index

        read(data_ex,ex_path)
        for i in range(len(data_ex)):
            f_string=mutant(data_ex[i],data)
            if f_string != "":
                num += 1
                data_s.append(data_ex[i])
                data_f.append(f_string)
                f3.write(str(index)+"  "+str(i+1)+"\n")

        index+=1
        write(data_f,f_path)
        write(data_s,s_path)
    f3.close()

    print("ok")
    print("test case num： %s" %num)