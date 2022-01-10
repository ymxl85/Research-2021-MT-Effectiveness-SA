"""
    +not
"""


def getnoun(path):
    word = {}
    f = open(path, 'r')
    for line in f:
        if line.find("Text=") and line.find("PartOfSpeech="):
            if line.find("Text=") != -11 and line.find("PartOfSpeech=") != -1:
                i1 = line.index("Text=")
                j1 = line.index("CharacterOffsetBegin")
                text = line[i1 + 5:j1 - 1]
                i1 = line.index("PartOfSpeech=")
                j1 = line.index("]")
                pos_s = line[i1 + 13:j1]
                if (pos_s == "VBP" or pos_s == "VBN") and (
                        text != "is" or text != "was" or text != "were" or text != "are"):
                    word = {text: pos_s}
                    break
    return word


def mutant(noun, sentence):
    f_sentence = ""
    position = -1
    flag_word = ""
    flag = 0
    if sentence.find(" is ") != -1:
        position = sentence.find(" is ")
        flag_word = " is "
        flag = 1
    elif sentence.find(" was ") != -1:
        position = sentence.find(" was ")
        flag_word = " was "
        flag = 1
    elif sentence.find(" are ") != -1:
        position = sentence.find(" are ")
        flag_word = " are "
        flag = 1
    elif sentence.find(" were ") != -1:
        position = sentence.find(" were ")
        flag_word = " were "
        flag = 1
    else:
        noun = (noun)
        noun1 = tuple(noun.keys())
        pos_noun = noun[noun1[0]]
        if sentence.find(" " + noun1[0] + " ") != -1:
            position = sentence.find(" " + noun1[0] + " ")
            flag_word = " " + noun1[0] + " "
            flag = 2
    if position != -1:
        if flag == 1:
            if sentence[position + len(flag_word):position + len(flag_word) + 4] != "not ":
                f_sentence = sentence[:position + len(flag_word)] + "not " + sentence[position + len(flag_word):]
        elif flag == 2:
            if pos_noun == "VBP":  # 第三人称单数 之前+ don't
                f_sentence = sentence[:position] + " don't" + sentence[position:]
            elif pos_noun == "VBN":  # 过去分词且前面有have/has/had，+not +VBN
                if sentence[position - 5:position + 1] == " have ":
                    f_sentence = sentence[:position] + " not" + sentence[position:]
                elif sentence[position - 4:position + 1] == " has ":
                    f_sentence = sentence[:position] + " not" + sentence[position:]
                elif sentence[position - 4:position + 1] == " had ":
                    f_sentence = sentence[:position] + " not" + sentence[position:]
    return f_sentence


def read(data, path):
    f = open(path, 'r')
    for string in f:
        data.append(string)
    f.close()


if __name__ == '__main__':
    index = 1
    count = 2000
    num = 0
    path1 = "E:/MT_SA/data/input/log_22.txt"  # 用来存储生成的follow-up文件
    f3 = open(path1, 'a')
    while index <= count:
        ex_path = "E:/MT_SA/data/input/source1/s%s.txt" % index
        s_path = "E:/MT_SA/data/input/mr2_2/s%s.txt" % index
        f_path = "E:/MT_SA/data/input/mr2_2/f%s.txt" % index
        ex_data = []
        f1 = open(s_path, 'w')
        f2 = open(f_path, 'w')
        read(ex_data, ex_path)

        for i in range(len(ex_data)):
            if ex_data[i].find("?") != len(ex_data[i])-3:
                pos_path = "E:/MT_SA/data/pos/output/s%s/s%s.txt.out" % (index, i + 1)
                res = getnoun(pos_path)
                #  print(index,i+1)
                if len(res) != 0 or ex_data[i].find(" is ") != -1 or ex_data[i].find(" was ") != -1 or ex_data[i].find(
                        " are ") != -1 or ex_data[i].find(" were ") != -1:
                    f_string = mutant(res, ex_data[i])
                    if f_string != "":
                        num += 1
                        log = str(index) + "  " + str(i + 1) + "\n"
                        f1.write(ex_data[i])
                        f2.write(f_string)
                        f3.write(log)
                        # print(ex_data[i])
                    # print(f_string)
        index += 1
        f1.close()
        f2.close()
    f3.close()

    print("ok")
    print("test case num： %s" % num)
