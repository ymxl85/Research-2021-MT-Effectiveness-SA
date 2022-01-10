"""
    置换句子的顺序
    将情感相同的句子放在一起
    document 级别的

    mr5_2
"""
import os


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


if __name__ == '__main__':
    index = 1
    count = 2000
    while index <= count:
        data_s = []
        data_os = []
        data_f = []
        # 分别存储 不同情感的数据
        data1 = []
        data2 = []
        data3 = []
        data4 = []
        s_path = "E:/MT_SA/data/input/mr5_2/azure/s%s.txt" % index
        if os.path.exists(s_path):
            f_path = "E:/MT_SA/data/input/mr5_2/azure/f%s.txt" % index
            os_path = "E:/MT_SA/data/output/source1/azure/os%s.txt" % index
            read(data_s, s_path)
            read(data_os, os_path)
            length_s = len(data_s)
            for i in range(length_s):
                sentiment = data_os[i].split("Positive=")[0].split("sentiment=")[1].strip()
                if sentiment == "negative":
                    data1.append(data_s[i])
                elif sentiment == "neutral":
                    data2.append(data_s[i])
                elif sentiment == "positive":
                    data3.append(data_s[i])
                else:
                    data4.append(data_s[i])

            if len(data1) != 0:
                data_f.extend(data1)
            if len(data2) != 0:
                data_f.extend(data2)
            if len(data3) != 0:
                data_f.extend(data3)
            if len(data4) != 0:
                data_f.extend(data4)

            write(data_f, f_path)
        index += 1
    print("ok")
