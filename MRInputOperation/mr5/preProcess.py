'''
    处理文件，保留文件size <= 5000 的存储到对应的 s ， os 文件夹下
'''


def write_path2path(path1, path2):
    p1 = open(path1, 'r')
    p2 = open(path2, 'w')
    for line1 in p1:
        p2.write(line1)
    p1.close()
    p2.close()


if __name__ == '__main__':
    index = 1
    case_num = 0
    mr = "mr7_2/herokuapp"
    while index <= 2000:
        data = []
        source_path = "E:/MT_SA/data/input/source1/s%s.txt" % index

        f = open(source_path, 'r')
        string = ""
        count = 0
        for line in f:
            string += line.strip()
            data.append(line)
        f.close()
        count = len(string)

        if count <= 5000:
            case_num += 1
            s_path = "E:/MT_SA/data/input/%s/s%s.txt" % (mr, index)
            write_path2path(source_path, s_path)
        index += 1
    print("OK")
    print(case_num)
