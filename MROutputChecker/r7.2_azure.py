"""
    azure
    检查 document_sentiment 的sentiment
    sentiment 一样
    mr7_2
"""

import os

def findPF(ts,fp):
    rdir0 = "E:/MT_SA_FS/data/txt_sentoken/neg/"
    rdir1 = "E:/MT_SA_FS/data/txt_sentoken/pos/"
    fts = open(ts,'r')
    ds = fts.readlines()
    for root, dirs, files in os.walk(rdir0):
        for cf in files:
            ff = os.path.join(root, cf)
            ffs = open(ff,'r')
            df = ffs.readlines()
            if ds == df:
                fp.write(ts + "------->" + ff + "\n")
                return "negative"
           # print(ff+"\n")
           # if filecmp.cmp(ts, ff):
           #     print(ts+"------->"+ff+"\n")
           #     return "NEGATIVE"
    for root, dirs, files in os.walk(rdir1):
        for cf in files:
            ff = os.path.join(root, cf)
            ffs = open(ff, 'r')
            df = ffs.readlines()
            if ds == df:
                fp.wrtie(ts + "------->" + ff + "\n")
                return "positive"
            #print(ff+"\n")
            #if filecmp.cmp(ts, ff):
            #    print(ts+"------->"+ff+"\n")
            #    return "POSITIVE"
            fts.close()
    return "NO"
def getinfo(data):
    sentiment = data[len(data) - 1].split("Positive=")[0].split("document_sentiment=")[1].strip()
    pos = data[len(data) - 1].split("Neutral=")[0].split("Positive=")[1].strip()
    neu = data[len(data) - 1].split("Negative=")[0].split("Neutral=")[1].strip()
    neg = data[len(data) - 1].split("Negative=")[1].strip()
    score = {"positive": pos, "negative": neg, "neutral": neu, "mix": 0}

    return sentiment, score


def check(text1, text2):
    s_sentiment = getinfo(text1)[0]
    s_dic = (getinfo(text1)[1])
    f_sentiment = getinfo(text2)[0]
    f_dic = (getinfo(text2)[1])
    if s_sentiment == "mixed" or s_sentiment == "neutral":
        flag = -1
    else:
        if s_sentiment == f_sentiment: # and abs(float(f_dic[f_sentiment]) - float(s_dic[s_sentiment])) <= 0.1:
            flag = 1
        else:
            flag = 0

    return flag


if __name__ == '__main__':
    index = 1
    file_num = 2000  # 测试用例总数
    false_num = 0
    case_num = 0
    fs_num = 0
    smr = "mr7_2"
    inputdir = "E:/MT_SA_FS/data/TestingResults/input/"
    outputDir = "E:/MT_SA_FS/data/TestingResults/output/"
    resultDir = "E:/MT_SA_FS/data/analysis/OSR2/dresult/"

    pp = resultDir + "0status.txt"
    ff = open(pp, 'a')
    path3 = resultDir + smr + "micro_0.txt"  # jmy
    path4 = resultDir + smr + "micro_1.txt"  # jmy
    path5 = resultDir + smr + "micro_1_fs.txt"  # jmy
    print(path3)
    f3 = open(path3, 'w')
    f4 = open(path4, 'w')
    f5 = open(path5, 'w')

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
            check_flag = check(data1, data2)
            if check_flag != -1:
                case_num += 1
                if check_flag == 0:
                    false_num += 1
                    f3.write(path1 + "\n" + data1[len(data1) - 1] + "\n" + data2[len(data2) - 1])
                    f3.write("\n------------------------*******************-----------------\n")
                else:
                    f4.write(path1 + "\n" + data1[len(data1) - 1] + "\n" + data2[len(data2) - 1])
                    f4.write("\n------------------------*******************-----------------\n")

                    tsfile = inputdir + smr + "/azure/s%s.txt" % index
                    # print("===================================" + tsfile + "\n")
                    truth = findPF(tsfile,f5)
                    real = getinfo(data1)[0]
                    print(truth + "----" + real +"\n")

                    if truth != real:
                        fs_num += 1
                        f5.write(path1 + "\n" + data1[len(data1) - 1] + "\n" + data2[len(data2) - 1])
                        f5.write("\n------------------------*******************-----------------\n")
        index += 1


    ff.write("microsoft-" + smr + "#MTG：" + str(case_num) + "\n")
    ff.write("microsoft-" + smr + "#SMTG:" + str(case_num - false_num) + "\n")
    ff.write("microsoft-" + smr + "#SR:" + str((case_num - false_num) / case_num) + "\n")
    ff.write("---------------microsoft-" + smr + "#FS:" + str(fs_num) + "\n")
    f3.close()
    f4.close()
    ff.close()
