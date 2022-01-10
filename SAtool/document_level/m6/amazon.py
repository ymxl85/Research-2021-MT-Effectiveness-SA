"""
    包含document_sentiment
"""

import boto3
import os

REGION_NAME = 'us-east-1'
ACCESS_KEY = "AKIAICSDDWB6XS4ODDQA"
SECRET_KEY = "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"


def sentiment_analisis(client, path1, path2):
    f1 = open(path1, "r", encoding='gb18030')
    f2 = open(path2, "w", encoding='UTF-8')
    # get document_sentiment
    string = ""
    for line in f1:
        f2.write(line)
        string += line.strip()

    response = client.batch_detect_sentiment(
        TextList=[string],
        LanguageCode='en'
    )

    f2.write("\n")

    res1 = response.get("ResultList")[0]
    f2.write("document_sentiment={}  ".format(res1.get("Sentiment")))
    f2.write(" Positive={0} Negative={1} Neutral={2} Mixed={3} ".format(
        res1.get("SentimentScore").get("Positive"),
        res1.get("SentimentScore").get("Negative"),
        res1.get("SentimentScore").get("Neutral"),
        res1.get("SentimentScore").get("Mixed"),
    ))
    f2.close()


if __name__ == '__main__':
    client = boto3.client('comprehend', region_name=REGION_NAME, aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
    index = 1
    case_num = 2000
    mr = "mr6_2/amazon"
    while index <= case_num:
        f_index = 1
        while f_index <= 10:
            f_path = "E:/MT_SA/data/input/%s/f%s_%s.txt" % (mr, index, f_index)
            if os.path.exists(f_path):
                of_path = "E:/MT_SA/data/output/%s/of%s_%s.txt" % (mr, index, f_index)
                sentiment_analisis(client, f_path, of_path)
            f_index += 1
        index += 1

    print("ok")
