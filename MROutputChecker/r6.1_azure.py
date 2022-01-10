"""
    情感逐渐趋向于 positive
    negative --> neutral -> positive
    情感相同时，分数应该时升高的
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
                fp.write(ts + "------->" + ff + "\n")
                return "positive"
            #print(ff+"\n")
            #if filecmp.cmp(ts, ff):
            #    print(ts+"------->"+ff+"\n")
            #    return "POSITIVE"
            fts.close()
    return "NO"

def getInfo(data):
    sentiment = data[len(data) - 1].split("Positive=")[0].split("document_sentiment=")[1].strip()
    pos = data[len(data) - 1].split("Neutral=")[0].split("Positive=")[1].strip()
    neu = data[len(data) - 1].split("Negative=")[0].split("Neutral=")[1].strip()
    neg = data[len(data) - 1].split("Negative=")[1].strip()
    score = {"positive": pos, "negative": neg, "neutral": neu, "mixed": 0}
    #print(data)
    #print("\n")
    #print(sentiment + str(score) +"\n")
    return sentiment, score


def check(ss, sc):
    if ss[0] == "mixed":
       return -1
    flag = 1
    for i in range(len(ss) - 2):
        ps = ss[i]
        pc = sc[i]
        ns = ss[i + 1]
        nc = sc[i + 1]
        if (ps == ns and ps == "negative" and float(pc) < float(nc)) or \
                (ps == ns and ps == "positive" and float(pc) > float(nc)) or \
                (ps == "positive" and ns != "positive") or \
                (ps == "mixed" and ns == "negative"):
            flag = 0
            break
    return flag




def write_file(path, path_s, sen, score):
    f3 = open(path, 'a')
    f3.write(path_s + "\n")
    f3.write("sentiment= " + str(sen))
    f3.write("\npositive_score= " + str(score))
    f3.write("\n-----------------------****------------------------\n")


if __name__ == '__main__':
    index = 1
    file_num = 2000
    false_num = 0
    case_num = 0

    fs_num = 0
    smr = "mr6_1"
    inputdir = "E:/MT_SA_FS/data/TestingResults/input/"
    outputDir = "E:/MT_SA_FS/data/TestingResults/output/"
    resultDir = "E:/MT_SA_FS/data/analysis/OSR0/dresult/"

    path3 = resultDir + smr + "micro_0.txt"  # jmy
    path4 = resultDir + smr + "micro_1.txt"  # jmy
    path5 = resultDir + smr + "micro_1_fs.txt"  # jmy
    f3 = open(path3, 'w')
    f4 = open(path4, 'w')
    f5 = open(path5, 'w')
    pp = resultDir + "0status.txt"
    ff = open(pp, 'a')

    while index <= file_num:
        sentiments = []
        scores = []
        path1 = outputDir + smr + "/azure/os%s.txt" % index
        if os.path.exists(path1):
            f1 = open(path1, 'r')
            text_s = f1.readlines()
            f1.close()
            info_s = getInfo(text_s)
            sa = info_s[0]
            scores.append(info_s[1][sa])
            sentiments.append(sa)

            f_index = 1
            while f_index <= 10:
                path2 = outputDir + smr + "/azure/of%s_%s.txt" % (index, f_index)
                f2 = open(path2, 'r')
                text_f = f2.readlines()
                f2.close()

                info_f = getInfo(text_f)
                sa = info_f[0]
                scores.append(info_f[1][sa])
                sentiments.append(sa)

                f_index += 1
            r = check(sentiments, scores)
            if r == 0:
                false_num += 1
                write_file(path3, path1, sentiments, scores)
                case_num += 1

                f3.write(path2 + "\n")
                f3.write("sentiment= " + str(sentiments))
                f3.write("\npositive_score= " + str(scores))
                f3.write("\n-----------------------****------------------------\n")
            elif r == 1:
                f4.write(path2 + "\n")
                f4.write("sentiment= " + str(sentiments))
                f4.write("\npositive_score= " + str(scores))
                f4.write("\n-----------------------****------------------------\n")
                case_num += 1

                tsfile = inputdir + smr + "/azure/s%s.txt" % index
                # print("==================================="+tsfile+"\n")
                truth = findPF(tsfile,f5)
                real = getInfo(text_s)[0]
                print(truth + "----" + real + "\n")

                if truth != real:
                    fs_num += 1
                    f5.write(path2 + "\n")
                    f5.write("sentiment= " + str(sentiments))
                    f5.write("\npositive_score= " + str(scores))
                    f5.write("\n-----------------------****------------------------\n")
        index += 1


    ff.write("micro-" + smr + "#MTG：" + str(case_num) + "\n")
    ff.write("micro-" + smr + "#SMTG:" + str(case_num - false_num) + "\n")
    ff.write("micro-" + smr + "#SR:" + str((case_num - false_num) / case_num) + "\n")
    ff.write("---------------micro-" + smr + "#FS:" + str(fs_num) + "\n")
