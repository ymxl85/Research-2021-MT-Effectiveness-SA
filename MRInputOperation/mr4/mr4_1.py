"""
    change tense

"""

import urllib.request
from bs4 import BeautifulSoup
import time
import socket


def getnoun(path):
    word = ""
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
                if pos_s == "VBP":
                    word = text
                    break
    return word


def get_past(old_word):
    past = ""
    try:
        url = "http://www.iciba.com/word?w=%s" % old_word
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.105 Safari/537.36'}
        socket.setdefaulttimeout(20)  # 设置socket层的超时时间为20秒
        time.sleep(15)
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        data = BeautifulSoup(response, 'html.parser')
        list1 = data.findAll('ul', attrs={'class': "Morphology_morphology__3g6fA"})
        if len(list1) != 0:
            list2 = list1[0].findAll('li')
            dict1 = {}
            for list_t in list2:
                text = list_t.get_text()
                tense = text.split(":")[0].strip()
                tense1 = text.split(":")[1].split(";")[0].strip("\xa0;")
                dict1.update({tense: tense1})
            if '过去式' in dict1:
                past = dict1["过去式"]
        response.close()
    except Exception as reason:
        print(reason)
    return past


def mutant(noun, sentence):
    f_sentence = ""
    past_word = get_past(noun)
    if past_word != "":
        if sentence.find(noun) != -1:
            if sentence.index(noun) == 0:
                noun = noun + " "
                past_word = past_word + " "
            else:
                noun = " " + noun + " "
                past_word = " " + past_word + " "
            f_sentence = sentence.replace(noun, past_word)
    else:
        f_sentence = ""
    return f_sentence


def read(data, path):
    f = open(path, 'r')
    for string in f:
        data.append(string)
    f.close()


if __name__ == '__main__':
    index = 1901
    count = 2000
    num = 17210
    path1 = "E:/MT_SA/data/input/log_41.txt"  # 用来存储生成的follow-up文件
    f3 = open(path1, 'a')
    while index <= count:
        ex_path = "E:/MT_SA/data/input/source1/s%s.txt" % index
        f_path = "E:/MT_SA/data/input/mr4_1/f%s.txt" % index
        s_path = "E:/MT_SA/data/input/mr4_1/s%s.txt" % index
        ex_data = []
        f1 = open(s_path, 'w')
        f2 = open(f_path, 'w')
        read(ex_data, ex_path)
        for i in range(len(ex_data)):
            pos_path = "E:/MT_SA/data/pos/output/s%s/s%s.txt.out" % (index, i + 1)
            res = getnoun(pos_path)
            print(index, i + 1)
            if len(res) != 0:
                ex_string = ex_data[i]
                f_string = mutant(res, ex_string)
                if f_string != "":
                    num += 1
                    f1.write(ex_data[i])
                    f2.write(f_string)
                    f3.write(str(index) + "  " + str(i + 1) + "\n")
                    # print(ex_data[i])
                    # print(f_string)
        index += 1
        f1.close()
        f2.close()
    f3.close()
    # write(s_data,s_path)

    print("ok")
    print("test case num： %s" % num)
