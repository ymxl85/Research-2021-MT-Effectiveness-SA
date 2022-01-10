import requests

url = 'https://sentim-api.herokuapp.com/api/v1/'
header = {"Accept": "application/json", "Content-Type": "application/json"}


def getSentiment(s):
    body = {"text": s}
    res = requests.post(url, headers=header, json=body).json()  # 获得结果

    out1 = str(res['result']["type"])
    out2 = str(res['result']["polarity"])
    return out1, out2


if __name__ == '__main__':
    count = 2000
    mr = "mr1_1"
    index = 3
    while index <= count:
        path1 = "E:/MT_SA/data1/input/%s/f%s.txt" % (mr, index)
        path2 = "E:/MT_SA/data1/output/%s/herokuapp/of%s.txt" % (mr, index)
        # path3 = "D:/eclipse-workspace/MT_SA/data/output/source1/herokuapp/os%s.txt"  %index
        f1 = open(path1, "r", encoding='gb18030')
        f2 = open(path2, 'w')
        # f3=open(path3,'w')

        if len(f1.read()) != 0:
            f1.seek(0)
            for sentence in f1:
                data = getSentiment(sentence)
                f2.write(sentence.strip("\n") + "   sentiment=" + str(data[0]) + "  polarity=" + str(data[1]) + "\n")
            #  f3.write(sentence.strip("\n")+"   sentiment="+str(data[0])+"  polarity="+str(data[1])+"\n")
            f2.close()
        f1.close()
        # f3.close()
        index += 1
print("it's OK！")
