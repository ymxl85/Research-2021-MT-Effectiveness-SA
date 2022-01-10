'''
        document_sentiment
'''

import requests

url = "http://text-processing.com/api/sentiment/"


def getSentiment(path1,path2):

    f1=open(path1,'r',encoding='gb18030')
    f2=open(path2,'w')
    text=""
    for line in f1:
        f2.write(line)
        text += line.strip()
    f1.close()
    data = {'text': text}
    results = requests.post(url, data=data).json()  # 获得结果
    f2.write("\n" + "document_sentiment= " + results["label"] +" negative={0} neutral={1} positive={2}".format(
                results["probability"]["neg"],
                results["probability"]["neutral"],
                results["probability"]["pos"],
            ))

    f2.close()


if __name__ == '__main__':
    index=1
    case_num=2000
    mr="mr5_1"

    while index<=case_num:
        in_path = "E:/MT_SA/data/input/%s/f%s.txt" %(mr,index)
        out_path ="E:/MT_SA/data/output/%s/nltk/of%s.txt" %(mr,index)
        getSentiment(in_path,out_path)
        index += 1

print("it's OK！")
