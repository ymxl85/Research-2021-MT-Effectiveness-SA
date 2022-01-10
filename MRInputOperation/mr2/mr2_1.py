"""
    Adding emphasizing adverbs

"""
import csv


def mutant(sentence, word_set):
    for j in range(len(word_set[1])):
        i1 = sentence.find(" " + word_set[1][j] + " ")
        if i1 != -1:
            f_sentence = sentence[:i1] + " " + word_set[0][j] + sentence[i1:]
            break
        else:
            f_sentence = ""

    return f_sentence


def getDict(path):
    with open(path, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        column1 = [row['Word'] for row in reader]
    csvfile.close()
    with open(path, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        column2 = [row['Phrase'] for row in reader]
    csvfile.close()
    return column1, column2


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
    path = "E:/MT_SA/MRelation/mr2/list.csv"
    count = 2000
    index = 1
    num = 0
    wordset = getDict(path)
    path1 = "E:/MT_SA/data/input/log_21.txt"  # 用来存储生成的follow-up文件
    f3 = open(path1, 'a')
    while index <= count:
        data_ex = []
        data_f = []
        data_s = []
        ex_path = "E:/MT_SA/data/input/source1/s%s.txt" % index
        f_path = "E:/MT_SA/data/input//mr2_1/f%s.txt" % index
        s_path = "E:/MT_SA/data/input//mr2_1/s%s.txt" % index

        read(data_ex, ex_path)

        for i in range(len(data_ex)):
            f_string = mutant(data_ex[i], wordset)
            if f_string != "":
                num += 1
                data_s.append(data_ex[i])
                data_f.append(f_string)
                f3.write(str(index) + "  " + str(i + 1) + "\n")
        index += 1
        write(data_f, f_path)
        write(data_s, s_path)
    f3.close()

    print("ok")
    print("test case num： %s" % num)
