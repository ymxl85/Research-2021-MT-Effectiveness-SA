"""
    处理文件，把 document sentiment写进os中
"""
import os


def write(data, path):
    f = open(path, 'w')
    for s1 in data:
        f.write(s1)
    f.close()


if __name__ == '__main__':
    index = 1
    case_num = 0
    mr = "mr7_2"
    web = "azure"
    while index <= 2000:
        os1_path = "E:/MT_SA/data/output/source2/%s/os%s.txt" % (web, index)
        if os.path.exists(os1_path):
            data1 = []
            os2_path = "E:/MT_SA/data/output/source1/%s/os%s.txt" % (web, index)
            os_path = "E:/MT_SA/data/output/%s/%s/os%s.txt" % (mr, web, index)
            f1 = open(os1_path, 'r')
            f2 = open(os2_path, 'r')
            for line1 in f2:
                data1.append(line1)
            data2 = f1.readlines()
            data1.append(data2[len(data2) - 2])
            data1.append(data2[len(data2) - 1])
            write(data1, os_path)
        index += 1
    print("OK")
