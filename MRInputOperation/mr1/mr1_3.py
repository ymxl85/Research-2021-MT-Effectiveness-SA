"""
    exchange between singulars and plurals


"""
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


def get_plural(old_word):
    plurals = ""
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
            dict = {}
            for list in list2:
                text = list.get_text()
                tense = text.split(":")[0].strip()
                tense1 = text.split(":")[1].split(";")[0].strip("\xa0;")
                dict.update({tense: tense1})
            if '复数' in dict:
                plurals = dict["复数"]
        response.close()
    except Exception as reason:
        print(reason)
    return plurals


def mutant(noun, sentence):
    f_sentence = ""
    singular = ""
    plural = ""
    end = len(sentence) - 1
    # 确定a/an/the的位置
    if sentence.find(" a ") != -1:
        a_index = sentence.find(" a ")
        flag = " a "
    elif sentence.find(" an ") != -1:
        a_index = sentence.find(" an ")
        flag = " an "
    else:
        a_index = -1
        flag = ""
    if a_index != -1:
        for s in range(a_index, len(sentence)):
            if not sentence[s].isalpha() and sentence[s] != " ":
                end = s
                break
        for i1 in range(len(noun)):
            n_index = sentence.find(" " + noun[i1] + " ")
            if n_index != -1 and a_index < n_index < end:
                if i1 != len(noun) - 1:
                    n1_index = sentence.find(" " + noun[i1 + 1] + " ")
                    if n1_index != -1 and n1_index == n_index + len(" " + noun[i1]):
                        singular = noun[i1 + 1]
                        singular_index = n1_index
                        plural = get_plural(singular)
                        break
                    else:
                        singular = noun[i1]
                        singular_index = n_index
                        plural = get_plural(singular)
                        break
                else:
                    singular = noun[i1]
                    singular_index = n_index
                    plural = get_plural(singular)
                    break
    # 寻找a/an 之前存在 is/was，将进行修改
    if plural != "":
        f_sentence = sentence[:a_index] + sentence[a_index + len(flag) - 1:singular_index] + " " + plural + sentence[singular_index + len(
                                                                                                                singular) + 1:]
        is_index = a_index - 1
        while is_index >= 2:
            if not f_sentence[is_index].isalpha() and f_sentence[is_index] != " ":
                f_sentence = f_sentence
                break
            else:
                #   print(f_sentence[is_index])
                if f_sentence[is_index - 1:is_index + 1] == "\'s":
                    f_sentence = f_sentence[:is_index - 1] + "\'re" + f_sentence[is_index + 1:]
                    break
                elif f_sentence[is_index - 2:is_index + 2] == " is ":
                    f_sentence = f_sentence[:is_index - 2] + " are" + f_sentence[is_index + 1:]
                    break
                elif f_sentence[is_index - 3:is_index + 2] == " was ":
                    f_sentence = f_sentence[:is_index - 3] + " were" + f_sentence[is_index + 1:]
                    break
            is_index -= 1
    return f_sentence


def read(data, path):
    f = open(path, 'r')
    for string in f:
        data.append(string)
    f.close()


if __name__ == '__main__':
    index = 1901
    count = 2000
    num = 21252
    path1 = "E:/MT_SA/data/input/log_13.txt"  # 用来存储生成的follow-up文件
    f3 = open(path1, 'a')
    while index <= count:
        ex_path = "E:/MT_SA/data/input//source1/s%s.txt" % index
        s_path = "E:/MT_SA/data/input/mr1_3/s%s.txt" % index
        f_path = "E:/MT_SA/data/input/mr1_3/f%s.txt" % index
        ex_data = []
        s_data = []
        f_data = []
        f1 = open(s_path, 'w')
        f2 = open(f_path, 'w')
        read(ex_data, ex_path)
        for i in range(len(ex_data)):
            if ex_data[i].find(" a ") != -1 or ex_data[i].find(" an ") != -1:  # if exist a/an，mutant it
                pos_path = "E:/MT_SA/data/pos/output/s%s/s%s.txt.out" % (index, i + 1)
                res = getnoun(pos_path)
                if len(res) != 0:
                    print(index, i + 1)
                    ex_string = ex_data[i]
                    f_string = mutant(res, ex_string)
                    if f_string != "":
                        num += 1
                        f1.write(ex_data[i])
                        f2.write(f_string)
                        f3.write(str(index) + "  " + str(i + 1) + "\n")
                    #   print(ex_data[i])
                    #   print(f_string)
        index += 1
        f1.close()
        f2.close()
    f3.close()

    print("ok")
    print("test case num： %s" % num)
