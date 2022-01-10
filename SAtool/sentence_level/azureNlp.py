"""
        只有 sentence.sentiment
        # 使用之后记得删除自己的key和endpoint
        # key = "<paste-your-text-analytics-key-here>"
        # endpoint = "<paste-your-text-analytics-endpoint-here>"
        # key="a52d66c200ce4e528c3223f0f41ffa1d"
        # key = "5ecae4440b2443d2848384b298776cee"
        # endpoint="https://zqf.cognitiveservices.azure.com/"
"""

key = "e0c341bd143c46ab91d0fc88011ef9ce"
endpoint = "https://zz3.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credential=ta_credential)
    return text_analytics_client


def sentiment_analysis_example(client, path1, path2):
    f1 = open(path1, "r", encoding='gb18030')
    f2 = open(path2, "w", encoding='UTF-8')

    for line in f1:
        documents = [line]
        # print(documents)
        response = client.analyze_sentiment(documents=documents)[0]
        # print(response)
        f2.write(line.strip("\n") + " sentiment={} ".format(
            response.sentiment) + " Positive={0} Neutral={1} Negative={2}".format(
            response.confidence_scores.positive,
            response.confidence_scores.neutral,
            response.confidence_scores.negative,
        ))
        f2.write("\n")
    f1.close()
    f2.close()


if __name__ == '__main__':
    client1 = authenticate_client()
    count = 2000
    index = 1806
    mr = "mr1_1"
    while index <= count:
        path_in = "E:/MT_SA/data1/input/%s/f%s.txt" % (mr, index)
        path_ou = "E:/MT_SA/data1/output/%s/azure/of%s.txt" % (mr, index)
        f = open(path_in, 'r')
        if len(f.read()) != 0:
            f.seek(0)
            f.close()
            sentiment_analysis_example(client1, path_in, path_ou)
        index += 1
    print("ok")
