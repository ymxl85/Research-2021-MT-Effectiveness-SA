"""
    置换句子的顺序
    将第一句移到最后一句
    document 级别的

    mr5_1
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
        s_path = "E:/MT_SA/data/input/mr5_1/s%s.txt" % index
        if os.path.exists(s_path):
            f_path = "E:/MT_SA/data/input/mr5_1/f%s.txt" % index
            read(data_s, s_path)
            string0 = data_s[0]
            length_s = len(data_s)
            for i in range(length_s - 1):
                data_s[i] = data_s[i + 1]
            data_s[length_s - 1] = string0
            write(data_s, f_path)
        index += 1
    print("ok")
