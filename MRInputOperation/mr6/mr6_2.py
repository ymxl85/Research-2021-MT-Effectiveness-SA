"""
    逐渐往 source 中添加 negative 的句子

"""
import os


def write(data, path):
    f = open(path, 'w')
    for s1 in data:
        f.write(s1)
    f.close()


def read(data, path):
    f = open(path, 'r')
    for s2 in f:
        data.append(s2)
    f.close()


if __name__ == '__main__':
    index = 1
    count = 2000
    web = "herokuapp"

    while index <= count:
        text = []
        data_s = []
        s_path = "E:/MT_SA/data/input/mr6_2/%s/s%s.txt" % (web, index)
        path_text = "E:/MT_SA/MRelation/mr6/negative_%s.txt" % web
        read(text, path_text)

        if os.path.exists(s_path):
            f_index = 1
            read(data_s, s_path)
            while f_index <= len(text):
                num = 0
                f_path = "E:/MT_SA/data/input/mr6_2/%s/f%s_%s.txt" % (web, index, f_index)
                data_f = []
                for line in data_s:
                    data_f.append(line)
                while num < f_index:
                    string = text[num]
                    data_f.append(string)
                    num += 1
                write(data_f, f_path)
                f_index += 1
        index += 1

    print("ok")
