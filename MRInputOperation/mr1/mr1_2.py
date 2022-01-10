"""
    synonyms

"""
import random
import urllib.request
from bs4 import BeautifulSoup
import time
import socket


def getnoun(path):
    word = []
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
                if pos_s == "NN":
                    word.append(text)
    return word


def get_synonyms(old_word):
    synonyms = ""
    try:
        url = "https://www.thesaurus.com/browse/%s" % old_word
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/84.0.4147.105 Safari/537.36'}
        socket.setdefaulttimeout(20)  # 设置socket层的超时时间为20秒
        time.sleep(15)
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        data = BeautifulSoup(response, 'html.parser')
        list1 = data.findAll('ul', attrs={'class': "css-1ytlws2 et6tpn80"})
        if len(list1) != 0:
            list2 = list1[0].findAll('li')
            synonyms = list2[0].find('a').get_text()
        response.close()
    # except urllib.error.HTTPError as reason:
    except Exception as reason:
        print(reason)
    return synonyms


def mutant(noun, sentence):
    f_sentence = ""
    noun_index = sentence.find(" " + noun + " ")
    if noun_index != -1:
        synonym = get_synonyms(noun)
        if synonym != "":
            if (synonym[0] == "a" or synonym[0] == "o" or synonym[0] == "e" or synonym[0] == "i" or synonym[0] == "u") \
                    and sentence[noun_index - 2:noun_index] == " a":
                f_sentence = sentence[:noun_index - 1] + "an " + synonym + sentence[noun_index + len(noun) + 1:]

            else:
                f_sentence = sentence[:noun_index] + " " + synonym + sentence[noun_index + len(noun) + 1:]
    return f_sentence


def read(data, path):
    f = open(path, 'r')
    for string in f:
        data.append(string)
    f.close()


if __name__ == '__main__':
    index = 601
    count = 622
    num = 32739
    path1 = "E:/MT_SA/data/input/log_12.txt"  # 用来存储生成的follow-up文件
    f3 = open(path1, 'a')
    while index <= count:
        ex_path = "E:/MT_SA/data/input//source1/s%s.txt" % index
        s_path = "E:/MT_SA/data/input/mr1_2/s%s.txt" % index
        f_path = "E:/MT_SA/data/input/mr1_2/f%s.txt" % index
        ex_data = []
        f1 = open(s_path, 'w')
        f2 = open(f_path, 'w')
        read(ex_data, ex_path)
        for i in range(len(ex_data)):
            pos_path = "E:/MT_SA/data/pos/output/s%s/s%s.txt.out" % (index, i + 1)
            res = getnoun(pos_path)
            if len(res) != 0:
                print(index, i + 1)
                ran = random.randint(0, len(res) - 1)
                s_string = ex_data[i]
                f_string = mutant(res[ran], s_string)
                if f_string != "":
                    num += 1
                    log = str(index) + "  " + str(i + 1) + "\n"
                    f1.write(ex_data[i])
                    f2.write(f_string)
                    f3.write(log)
        index += 1
        f1.close()
        f2.close()
    f3.close()

    print("ok")
    print("test case num： %s" % num)
