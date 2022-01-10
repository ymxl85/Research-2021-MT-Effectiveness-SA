"""
    处理文件，保留文件 source 和list数据 size <= 5000 的存储到对应的 s ， os 文件夹下
"""
import os

def write_path2path(path1, path2):
    p1 = open(path1, 'r')
    p2 = open(path2, 'w')
    for s in p1:
        p2.write(s)
    p1.close()
    p2.close()


if __name__ == '__main__':
    index = 1
    case_num = 0
    web = "azure"
    string1 = ""
    text_path = "E:/MT_SA/MRelation/mr6/positive_%s.txt" % web
    f1 = open(text_path, 'r')
    for line in f1:
        string1 += line.strip()
    f1.close()

    while index <= 2000:
        data = []
        source_path = "E:/MT_SA/data/input/source2/s%s.txt" % index
        if os.path.exists(source_path):
            count = 0
            f = open(source_path, 'r')
            string = ""
            for line in f:
                string += line.strip()
                data.append(line)
            f.close()

            count = len(string1) + len(string)

            if count <= 5000:
                case_num += 1
                s_path = "E:/MT_SA/data/input/mr6_1/%s/s%s.txt" % (web, index)
                os_path = "E:/MT_SA/data/output/mr6_1/%s/os%s.txt" % (web, index)
                osource_path = "E:/MT_SA/data/output/source2/%s/os%s.txt" % (web, index)
                write_path2path(source_path, s_path)
                write_path2path(osource_path, os_path)
        index += 1

    print("OK")
    print(case_num)
