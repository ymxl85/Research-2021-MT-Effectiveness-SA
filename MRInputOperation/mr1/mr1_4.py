"""
    将 .改变为！（只改句子末尾的 句点 ）
    sentence 级别
    57663
"""


def mutant(sentence):
    f_sentence = ""
    tag_word = " . \n"
    new_word = " ! \n"
    if sentence.find(tag_word) != -1 and sentence.find(" . . . \n") == -1:
        f_sentence = sentence.replace(tag_word, new_word)

    return f_sentence


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
    path1 = "E:/MT_SA/data/input/log_14.txt"  # 用来存储生成的follow-up文件
    f3 = open(path1, 'a')
    while index <= count:
        data_ex = []
        data_f = []
        data_s = []
        ex_path = "E:/MT_SA/data/input/source1/s%s.txt" % index
        f_path = "E:/MT_SA/data/input/mr1_4/f%s.txt" % index
        s_path = "E:/MT_SA/data/input/mr1_4/s%s.txt" % index
        read(data_ex, ex_path)

        for i in range(len(data_ex)):
            f_string = mutant(data_ex[i])
            if f_string != "":
                num += 1
                data_f.append(f_string)
                data_s.append(data_ex[i])
                f3.write(str(index) + "  " + str(i + 1) + "\n")

        index += 1

        write(data_f, f_path)
        write(data_s, s_path)
    f3.close()

    print(num)
    print("OK")
