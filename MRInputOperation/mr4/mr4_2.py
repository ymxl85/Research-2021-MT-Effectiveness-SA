"""
    swap words between (and or)
    5577
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
                if pos_s == "NN" or pos_s == "NNS" or pos_s == "NNP" or pos_s == "NNPS" or pos_s == "JJ" or pos_s == "JJS" or pos_s == "JJR":
                    temp = {text: pos_s}
                    word.update(temp)
    return word


def mutant(noun, sentence):
    f_sentence = ""
    noun = (noun)
    word = sentence.split(" ")
    for w in range(len(word)):
        if word[w] == "and" or word[w] == "or":
            word1 = word[w - 1]
            word2 = word[w + 1]
            if word1 in noun and word2 in noun and noun[word1] == noun[word2]:
                if sentence.find(word1) == 0:
                    # i1 = sentence.find(word1 + " ")
                    i2 = sentence.index(" " + word2 + " ") + len(" " + word2)
                    f_sentence = word2 + " " + word[w] + " " + word1 + sentence[i2:]
                elif sentence.find(word1) > 0:
                    i1 = sentence.index(" " + word1 + " ")
                    i2 = sentence.index(" " + word2 + " ") + len(" " + word2)
                    f_sentence = sentence[:i1] + " " + word2 + " " + word[w] + " " + word1 + sentence[i2:]
            break
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
    path1 = "D:/eclipse-workspace/MT_SA/data1/log_42.txt"  # 用来存储生成的follow-up文件
    f3 = open(path1, 'a')
    while index <= count:
        ex_path = "D:/eclipse-workspace/MT_SA/data/input/source1/s%s.txt" % index
        f_path = "D:/eclipse-workspace/MT_SA/data1/mr4_2/f%s.txt" % index
        s_path = "D:/eclipse-workspace/MT_SA/data1/mr4_2/s%s.txt" % index
        ex_data = []
        read(ex_data, ex_path)
        f1 = open(s_path, 'w')
        f2 = open(f_path, 'w')
        for i in range(len(ex_data)):
            if ex_data[i].find(" and ") != -1 or ex_data[i].find(" or ") != -1:
                pos_path = "D:/SentimentAnalysis/data/pos1/pos/output/s%s/s%s.txt.out" % (index, i + 1)
                res = getnoun(pos_path)
                if len(res) != 0:
                    f_string = mutant(res, ex_data[i])
                    if f_string != "":
                        num += 1
                        f1.write(ex_data[i])
                        f2.write(f_string)
                        f3.write(str(index) + "  " + str(i + 1) + "\n")
        index += 1
        # write(s_data,s_path)
        # print(index,num)
        f1.close()
        f2.close()
    f3.close()

    print("ok")
    print("test case num： %s" % num)
