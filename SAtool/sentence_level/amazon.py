import boto3

REGION_NAME = 'us-east-1'
ACCESS_KEY = "AKIAICSDDWB6XS4ODDQA"
SECRET_KEY = "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"


def sentiment_analisis(client, path1, path2):
    f1 = open(path1, "r", encoding='gb18030')
    f2 = open(path2, "w", encoding='UTF-8')
    for sentence in f1:
        # return dict
        response = client.batch_detect_sentiment(
            TextList=[sentence],
            LanguageCode='en'
            # LanguageCode='en'|'es'|'fr'|'de'|'it'|'pt'|'ar'|'hi'|'ja'|'ko'|'zh'|'zh-TW'
        )
        res = response.get("ResultList")[0]
        f2.write(format(sentence.strip("\n") + " sentiment=") + format(
            res.get("Sentiment") + " " + "Positive={0} Negative={1} Neutral={2} Mixed={3} ".format(
                res.get("SentimentScore").get("Positive"),
                res.get("SentimentScore").get("Negative"),
                res.get("SentimentScore").get("Neutral"),
                res.get("SentimentScore").get("Mixed")
            )))
        f2.write("\n")
    f1.close()
    f2.close()


if __name__ == '__main__':
    client = boto3.client('comprehend', region_name=REGION_NAME, aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
    count = 1
    index = 1
    # mr = "mr4_1"
    while index <= count:
        # path1 = "E:/MT_SA/data/input/%s/f%s.txt" % (mr, index)
        # path2 = "E:/MT_SA/data/output/%s/amazon/of%s.txt" % (mr, index)
        path1 = "E:/MT_SA/data1/input/data.txt"
        path2 = "E:/MT_SA/data1/input/odata.txt"
        # path1 = "D:/SentimentAnalysis/data/input/%s/amazon/f%s.txt"  %(mr,index)
        # path2 = "D:/SentimentAnalysis/data/output/%s/amazon/of%s.txt" %(mr,index)
        f = open(path1, 'r')
        if len(f.read()) != 0:
            f.seek(0)
            f.close()
            sentiment_analisis(client, path1, path2)
        index += 1

    print("ok")
