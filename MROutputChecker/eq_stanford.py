"""
   mr1_1,mr1_2,mr1_3,mr3_1,mr4_1,mr4_2,mr4_3,mr4_4
   check A2.label == A2.label
   满足为1
"""
import os
import argparse


def check(d1, d2):
    sentiment1 = d1.split("sentiment=")[1].strip()

    sentiment2 = d2.split("sentiment=")[1].strip()

    if sentiment1 == sentiment2:
        flag = 1
    else:
        flag = 0

    return flag


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--MR", type=str, default="0")
    args = parser.parse_args()
    smr = args.MR  # mr1_1 mr1_2 mr1_3 mr3_1 mr4_1 mr4_2 mr4_3 mr4_4

    outputDir = "E:/MT_SA_FS/data/TestingResults/output/"
    resultDir = "E:/MT_SA_FS/data/analysis/OSR2/sresult/"

    count = 2000  # 文件数
    index = 1
    case_num = 0  # 统计测试用例个数（该mr下句子数）
    false_num = 0  # 正确测试用例个数（该mr下通过测试用例个数）
    #mr = "mr1_1"
    pp = resultDir + "0status.txt"
    ff = open(pp, 'a')
    path3 = resultDir + smr + "stanford_0.txt"  # jmy
    path4 = resultDir + smr + "stanford_1.txt"  # jmy
    f3 = open(path3, 'w')
    f4 = open(path4, 'w')
    while index <= count:
        path1 = outputDir + "%s/stanford/os%s.txt" % (smr, index)
        path2 = outputDir + "%s/stanford/of%s.txt" % (smr, index)
        if os.path.exists(path1) and os.path.exists(path2):
            data1 = []
            data2 = []
            with open(path1) as f1:
                for line in f1:
                    data1.append(line)
            f1.close()
            with open(path2) as f2:
                for line in f2:
                    data2.append(line)
            f2.close()
            for j in range(len(data1)):
                case_num += 1
                if check(data1[j], data2[j]) == 0:
                    false_num += 1
                    f3.write("source= " + data1[j])
                    f3.write("follow_up= " + data2[j])
                    f3.write("-------------------------------------/////--------------------------------------------\n")
                else:
                    f4.write("source= " + data1[j])
                    f4.write("follow_up= " + data2[j])
                    f4.write("-------------------------------------/////--------------------------------------------\n")
        index += 1


    ff.write("stanford-" + smr + "#MTG: " + str(case_num) + "\n")
    ff.write("stanford-" + smr + "#SMTG: " + str(case_num - false_num) + "\n")
    ff.write("stanford-" + smr + "#SR: " + str((case_num - false_num) / case_num) + "\n")
    f3.close()
    f4.close()
    ff.close()
