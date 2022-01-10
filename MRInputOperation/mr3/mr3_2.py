'''
    Partially capitalization
    pos --> nouns and adjectives
    63116

'''
def getinfo(path):
    word_set=[]
    f=open(path,'r')
    for line in f:
        if line.find("Text=") and line.find("PartOfSpeech=") :
            if line.find("Text=")!=-11 and line.find("PartOfSpeech=")!=-1 :
                i0=line.index("Text=")
                j0=line.index("CharacterOffsetBegin")
                text=line[i0+5:j0-1]
                i1=line.index("PartOfSpeech=")
                j1=line.index("]")
                pos_s=line[i1+13:j1]
                if pos_s =="JJ" or pos_s=="JJR" or pos_s=="JJS" or pos_s=="NN" or pos_s == "NNS" or pos_s=="NNP" or pos_s=="NNPS" :
                    word_set.append(text)
    return word_set

def mutant(info,sentence):
    f_sentence=""
    if len(info) !=0:
        for j in range(len(info)):
            if sentence.find(info[j])!=-1:
                if sentence.index(info[j])==0:
                    word=info[j]+" "
                    sentence=sentence.replace(word,word.upper(),1)
                else:
                    word=" "+info[j]+" "
                    sentence=sentence.replace(word,word.upper(),1)
        f_sentence=sentence
    return f_sentence


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
    index=1
    count=2000
    num=0
    path1="D:/eclipse-workspace/MT_SA/data1/log_32.txt"  # 用来存储生成的follow-up文件
    f3=open(path1,'a')
    while index <= count:
        data_ex=[]
        data_s=[]
        data_f=[]
        ex_path = "D:/eclipse-workspace/MT_SA/data/input/source1/s%s.txt" %index
        f_path = "D:/eclipse-workspace/MT_SA/data1/mr3_2/f%s.txt" %index
        s_path = "D:/eclipse-workspace/MT_SA/data1/mr3_2/s%s.txt" %index

        read(data_ex,ex_path)

        for i in range(len(data_ex)):
            pos_path="D:/SentimentAnalysis/data/pos1/pos/output/s%s/s%s.txt.out" %(index,i+1)
            res=getinfo(pos_path)
            s_string=data_ex[i]
            f_string=mutant(res,s_string)
            if f_string != "":
                num+=1
                data_f.append(f_string)
                data_s.append(s_string)
                f3.write(str(index)+"  "+str(i+1)+"\n")
        index+=1
        write(data_f,f_path)
        write(data_s,s_path)
    f3.close()

    print("ok")
    print("test case num： %s" %num)