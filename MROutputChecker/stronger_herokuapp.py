"""
   mr2_1
   check A2.label == A1.label 且 A2.score >= A1.score
   满足为1
"""
import os
import argparse


def check(d1, d2):
    sentiment1 = d1.split("polarity=")[0].split("sentiment=")[1].strip()
    score1 = d1.split("polarity=")[1].strip()

    sentiment2 = d2.split("polarity=")[0].split("sentiment=")[1].strip()
    score2 = d2.split("polarity=")[1].strip()

    if sentiment1 == "neutral":
        flag = -1
    else:
        s2 = abs(float(score2))
        s1 = abs(float(score1))
        if sentiment1 == sentiment2 and (abs(s2) > abs(s1) or (abs(s2) == abs(s1) and abs(s2) == 1)): #(s2 - s1 > 0.1 or (s2 == s1 and s2 == 1)):
            flag = 1
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

    count = 2000  # 文件数
    index = 1
    case_num = 0  # 统计测试用例个数（该mr下句子数）
    false_num = 0  # 正确测试用例个数（该mr下通过测试用例个数）
    invalid_num = 0
    pp = resultDir + "0status.txt"
    ff = open(pp, 'a')
    path3 = resultDir + smr + "hk_0.txt"  # jmy
    path4 = resultDir + smr + "hk_1.txt"  # jmy
    f3 = open(path3, 'w')
    f4 = open(path4, 'w')
    while index <= count:
        # _output
        path1 = outputDir + smr + "/herokuapp/os%s.txt" % index
        path2 = outputDir + smr + "/herokuapp/of%s.txt" % index
        if os.path.exists(path1) and os.path.exists(path2):
            f1 = open(path1, 'r')
            data1 = f1.readlines()
            f1.close()
            # follow_up_output
            f2 = open(path2, 'r')
            data2 = f2.readlines()
            f2.close()
            # error
            for j in range(len(data2)):
                case_num += 1
                r = check(data1[j], data2[j])
                if r == 0:
                    false_num += 1
                    f3.write(path1 + "\n" + data1[j] + data2[j])
                    f3.write("\n------------------------*******************-----------------\n")
                if r == 1:
                    f4.write(path1 + "\n" + data1[j] + data2[j])
                    f4.write("\n------------------------*******************-----------------\n")
                if r == -1:
                    invalid_num += 1
        index += 1

    ff.write("hk-" + smr + "#Valid MTG：" + str(case_num - invalid_num) + "\n")
    ff.write("hk-" + smr + "#SMTG: " + str(case_num - invalid_num - false_num) + "\n")
    ff.write("hk-" + smr + "SR: " + str((case_num - invalid_num - false_num) / (case_num - invalid_num)) + "\n")
    f3.close()
    f4.close()
    ff.close()
