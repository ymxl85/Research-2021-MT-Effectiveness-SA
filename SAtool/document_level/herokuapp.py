"""
    将source存储为有document_sentiment
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
    document_sentiment = result['result']["type"]
    document_score = str(result['result']["polarity"])
    f2.write("\n" + "document_sentiment= " + document_sentiment + " polarity= " + document_score)

    f2.close()


if __name__ == '__main__':
    index = 1
    case_num = 2000  # 测试用例总数
    mr = "mr7_1"
    while index <= case_num:
        in_path = "E:/MT_SA/data/input/%s/herokuapp/f%s.txt" % (mr, index)
        if os.path.exists(in_path):
            f = open(in_path, 'r')
            if len(f.read()) != 0:
                f.seek(0)
                f.close()
                out_path = "E:/MT_SA/data/output/%s/herokuapp/of%s.txt" % (mr, index)
                getSentiment(in_path, out_path)
        index += 1

print("it's OK！")
