'''
    将soure全部转化为大写，生成followup
    sum=64720

'''


def write(data, path):
    f = open(path, 'w')
    for string in data:
        f.write(string)
    f.close()


def read(data, path):
    f = open(path, 'r')
    for string in f:
        data.append(string)
    f.close()


if __name__ == '__main__':
    # source followup
    index = 1
    count = 2000
    num = 0
    while index <= count:
        data_ex = []
        data_f = []
        data_s = []
        ex_path = "D:/eclipse-workspace/MT_SA/data/input/source1/s%s.txt" % index
        f_path = "D:/eclipse-workspace/MT_SA/data1/mr3_1/f%s.txt" % index
        s_path = "D:/eclipse-workspace/MT_SA/data1/mr3_1/s%s.txt" % index

        read(data_ex, ex_path)

        for i in range(len(data_ex)):
            num += 1
            data_f.append(data_ex[i].upper())
            data_s.append(data_ex[i])
        index += 1

        write(data_f, f_path)
        write(data_s, s_path)
    print("OK")
    print(num)
