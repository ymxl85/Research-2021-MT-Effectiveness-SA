""""
    but - although
"""


def mutant(sentence):
    f_sentence = ""
    position = sentence.find(" but ")
    if sentence[position - 1] == "." or sentence[position-1] == "," and sentence[0] != "(":
        f_sentence = "although " + sentence[:position] + " " + sentence[position+5:]
    return f_sentence


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
    num = 0
    path1 = "E:/MT_SA/data/input/log_43.txt"  # 用来存储生成的follow-up文件
    f3 = open(path1, 'a')
    while index <= count:
        ex_path = "E:/MT_SA/data/input/source1/s%s.txt" % index
        f_path = "E:/MT_SA/data/input/mr4_3/f%s.txt" % index
        s_path = "E:/MT_SA/data/input/mr4_3/s%s.txt" % index
        ex_data = []
        read(ex_data, ex_path)
        f1 = open(s_path, 'w')
        f2 = open(f_path, 'w')
        for i in range(len(ex_data)):
            if ex_data[i].find(" but ") != -1:
                f_string = mutant(ex_data[i])
                if f_string != "":
                    num += 1
                    f1.write(ex_data[i])
                    f2.write(f_string)
                    f3.write(str(index) + "  " + str(i + 1) + "\n")

        index += 1
        f1.close()
        f2.close()
    f3.close()

    print("ok")
    print("test case num： %s" % num)
