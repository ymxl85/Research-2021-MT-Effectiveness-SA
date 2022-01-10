"""
    将source存储为有document_sentiment 和 sentence_sentiment 的
"""

import requests
import os

url = 'https://sentim-api.herokuapp.com/api/v1/'
header = {"Accept": "application/json", "Content-Type": "application/json"}


def getSentiment(path1, path2):
    f1 = open(path1, 'r', encoding='gb18030')
    f2 = open(path2, 'w')
    # get document_sentiment
    string = ""
    for line in f1:
        f2.write(line)
        string += line.strip()
    body = {"text": string}
    result = requests.post(url, headers=header, json=body).json()  # 获得结果
    # print(result)
    document_sentiment = result['result']["type"]
    document_score = str(result['result']["polarity"])
    f2.write("\n" + "document_sentiment= " + document_sentiment + " polarity= " + document_score)

    f2.close()


if __name__ == '__main__':
    index = 1227
    case_num = 2000  # 测试用例总数
    mr = "mr6_2/herokuapp"
    while index <= case_num:
        f_index = 1
        while f_index <= 10:
            f_path = "E:/MT_SA/data/input/%s/f%s_%s.txt" % (mr, index, f_index)
            if os.path.exists(f_path):
                of_path = "E:/MT_SA/data/output/%s/of%s_%s.txt" % (mr, index, f_index)
                getSentiment(f_path, of_path)
            f_index += 1
        index += 1

print("it's OK！")
