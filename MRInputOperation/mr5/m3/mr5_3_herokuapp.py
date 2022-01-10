"""
    置换句子的顺序
    将情感相同的句子放在一起
    document 级别的

    mr5_2
"""
import os


def getInfo(d1):
    sentiment0 = d1.split("polarity=")[0].split("sentiment=")[1].strip()
    score0 = d1.split("polarity=")[1].strip()

    return sentiment0, score0


def read(data, path):
    f = open(path, 'r')
    for string in f:
        data.append(string)
    f.close()


def write(data, path):
    f = open(path, 'w')
    for string in data:
        f.write(string)
    f.close()


def descend(d, s):
    text = zip(s, d)
    text = sorted(text, reverse=True)
    scores, data = zip(*text)
    return list(data)


if __name__ == '__main__':
    index = 1
    count = 2000
    while index <= count:
        data_s = []
        data_os = []
        data_f = []
        # 分别存储 不同情感的数据
        data1 = []
        score1 = []
        data2 = []
        score2 = []
        data3 = []
        score3 = []
        data4 = []
        score4 = []
        s_path = "E:/MT_SA/data/input/mr5_3/herokuapp/s%s.txt" % index
        if os.path.exists(s_path):
            f_path = "E:/MT_SA/data/input/mr5_3/herokuapp/f%s.txt" % index
            os_path = "E:/MT_SA/data/output/source1/herokuapp/os%s.txt" % index
            read(data_s, s_path)
            read(data_os, os_path)
            length_s = len(data_s)
            for i in range(length_s):
                info = getInfo(data_os[i])
                sentiment = info[0]
                score = info[1]
                # data_s[i]=sentiment+"  "+score+"  "+data_s[i]
                if sentiment == "negative":
                    data1.append(data_s[i])
                    score1.append(score)
                elif sentiment == "neutral":
                    data2.append(data_s[i])
                    score2.append(score)
                elif sentiment == "positive":
                    data3.append(data_s[i])
                    score3.append(score)
                else:
                    data4.append(data_s[i])
                    score4.append(score)
            if len(data1) != 0:
                data_f.extend(descend(data1, score1))
            if len(data2) != 0:
                data_f.extend(descend(data2, score2))
            if len(data3) != 0:
                data_f.extend(descend(data3, score3))
            if len(data4) != 0:
                data_f.extend(descend(data4, score4))
            write(data_f, f_path)
        index += 1
    print("ok")
