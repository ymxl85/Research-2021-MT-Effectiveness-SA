"""
    amazon
    检查 document_sentiment
    应该是不变的
    mr1_1
"""
import os
import argparse


def getinfo(data):
    sentiment = data.split("Positive=")[0].split("sentiment=")[1].strip()
    pos = data.split("Negative=")[0].split("Positive=")[1].strip()
    neg = data.split("Neutral=")[0].split("Negative=")[1].strip()
    neu = data.split("Mixed=")[0].split("Neutral=")[1].strip()
    mix = data.split("Mixed=")[1].strip()

    score = {"POSITIVE": pos, "NEGATIVE": neg, "NEUTRAL": neu, "MIXED": mix}

    return sentiment, score


def check(text1, text2):
    s_sentiment = getinfo(text1)[0]
    s_dic = (getinfo(text1)[1])
    f_sentiment = getinfo(text2)[0]
    f_dic = (getinfo(text2)[1])
    #if s_sentiment == f_sentiment and abs(float(f_dic["POSITIVE"]) - float(s_dic["POSITIVE"])) <= 0.1 and abs(
    #       float(f_dic["NEGATIVE"]) - float(s_dic["NEGATIVE"])) <= 0.1 \
    #       and abs(float(f_dic["NEUTRAL"]) - float(s_dic["NEUTRAL"])) <= 0.1 and abs(float(f_dic["MIXED"]) -
    #       float(s_dic["MIXED"])) <= 0.1:
    if s_sentiment == f_sentiment: #and abs(float(f_dic[f_sentiment]) - float(s_dic[s_sentiment])) <= 0.1: #jmy
        flag = 1
    else:
        flag = 0

    return flag


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--MR", type=str, default="0")
    args = parser.parse_args()
    smr = args.MR # mr1_1 mr1_2 mr1_3 mr3_1 mr4_1 mr4_2 mr4_3 mr4_4

    outputDir = "E:/MT_SA_FS/data/TestingResults/output/"
    resultDir = "E:/MT_SA_FS/data/analysis/OSR2/sresult/"

    index = 1
    file_num = 2000
    false_num = 0
    case_num = 0  # 测试用例总数
    pp = resultDir + "0status.txt"
    ff = open(pp, 'a')
    path3 = resultDir + smr + "amazon_0.txt"  # jmy
    path4 = resultDir + smr + "amazon_1.txt"  # jmy
    f3 = open(path3, 'w')
    f4 = open(path4, 'w')
    while index <= file_num:
        # source_output
        path1 = outputDir + smr + "/amazon/os%s.txt" % index
        path2 = outputDir + smr + "/amazon/of%s.txt" % index
        if os.path.exists(path1) and os.path.exists(path2):
            f1 = open(path1, 'r')
            data1 = f1.readlines()
            f1.close()
            f2 = open(path2, 'r')
            data2 = f2.readlines()
            f2.close()

            # error

            for i in range(len(data2)):
                case_num += 1
                if check(data1[i], data2[i]) == 0:
                    false_num += 1
                    f3.write(path1 + "\n" + data1[i] + data2[i])
                    f3.write("\n------------------------*******************-----------------\n")
                else:
                    f4.write(path1 + "\n" + data1[i] + data2[i])
                    f4.write("\n------------------------*******************-----------------\n")
        index += 1

    ff.write("amazon-" + smr + "#MTG: " + str(case_num)+"\n")
    ff.write("amazon-" + smr + "#SMTG: " + str(case_num-false_num)+"\n")
    ff.write("amazon-" + smr + "#SR: " + str((case_num-false_num)/case_num)+"\n")


    f3.close()
    f4.close()
    ff.close()
