"""
    stronger sentiment for azure
    mixed 将不被考虑

"""
import os
import argparse


def getinfo(data):
    sentiment = data.split("Positive=")[0].split("sentiment=")[1].strip()
    pos = data.split("Neutral=")[0].split("Positive=")[1].strip()
    neu = data.split("Negative=")[0].split("Neutral=")[1].strip()
    neg = data.split("Negative=")[1].strip()
    score = {"positive": pos, "negative": neg, "neutral": neu}

    return sentiment, score


def check(text1, text2):
    s_sentiment = getinfo(text1)[0]
    s_dic = (getinfo(text1)[1])
    f_sentiment = getinfo(text2)[0]
    f_dic = (getinfo(text2)[1])
    # flag = -1 ; 该句子不考虑为测试用例
    if s_sentiment != "positive" and s_sentiment != "negative":
        flag = -1
    else:
        if s_sentiment == f_sentiment:
            s2 = float(f_dic[f_sentiment])
            s1 = float(s_dic[s_sentiment])
            if abs(s2) > abs(s1) or (s2 == s1 and s2 == 1): #s2 - s1 > 0.1 or (s2 == s1 and s2 == 1):
              flag = 1
            else:
                flag = 0
        else:
            flag = 0

    return flag


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--MR", type=str, default="0")
    args = parser.parse_args()
    smr = args.MR  # mr1_4 mr2_1 mr3_2

    outputDir = "E:/MT_SA_FS/data/TestingResults/output/"
    resultDir = "E:/MT_SA_FS/data/analysis/OSR2/sresult/"

    index = 1
    file_num = 2000
    false_num = 0
    case_num = 0  # 测试用例总数
    invalid_num = 0
    pp = resultDir + "0status.txt"
    ff = open(pp, 'a')
    path3 = resultDir + smr + "micro_0.txt"  # jmy
    path4 = resultDir + smr + "micro_1.txt"  # jmy
    f3 = open(path3, 'w')
    f4 = open(path4, 'w')
    while index <= file_num:
        # source_output
        path1 = outputDir + smr + "/azure/os%s.txt" % index
        path2 = outputDir + smr + "/azure/of%s.txt" % index
        if os.path.exists(path1) and os.path.exists(path2):
            f1 = open(path1, 'r')
            data1 = f1.readlines()
            f1.close()

            f2 = open(path2, 'r')
            data2 = f2.readlines()
            f2.close()
            # error
            for i in range(len(data2)):
                check_flag = check(data1[i], data2[i])
                case_num += 1
                if check_flag == 0:
                    false_num += 1
                    f3.write(path1 + "\n" + data1[i] + "\n" + data2[i])
                    f3.write("\n------------------------*******************-----------------\n")
                if check_flag == 1:
                    f4.write(path1 + "\n" + data1[i] + data2[i])
                    f4.write("\n------------------------*******************-----------------\n")
                if check_flag == -1:
                    invalid_num += 1
        index += 1





    ff.write("microsoft-" + smr + "#Valid MTG：" + str(case_num - invalid_num) + "\n")
    ff.write("microsoft-" + smr + "#SMTG: " + str(case_num - invalid_num - false_num) + "\n")
    ff.write("microsoft-" + smr + "SR: " + str((case_num - invalid_num - false_num) / (case_num - invalid_num)) + "\n")
    f3.close()
    f4.close()
    ff.close()
