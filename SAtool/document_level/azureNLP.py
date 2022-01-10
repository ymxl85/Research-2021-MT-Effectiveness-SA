"""
    包含document_sentiment
"""
key = "de978e351ffc4efa9cc3c1ff66846893"
endpoint = "https://zz3.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os


def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credential=ta_credential)
    return text_analytics_client


def sentiment_analysis_example(client, path1, path2):
    f1 = open(path1, "r", encoding='gb18030')
    f2 = open(path2, "w", encoding='UTF-8')
    string = ""
    for line in f1:
        f2.write(line)
        string += line.strip("\n")
    documents = [string]
    response = client.analyze_sentiment(documents=documents)[0]

    f2.write(
        "\n" + "document_sentiment={} ".format(response.sentiment) + " Positive={0} Neutral={1} Negative={2}".format(
            response.confidence_scores.positive,
            response.confidence_scores.neutral,
            response.confidence_scores.negative,
        ))
    f1.close()
    f2.close()


if __name__ == '__main__':
    client = authenticate_client()
    index = 1
    case_num = 2000
    mr = "mr7_2"
    while index <= case_num:
        in_path = "E:/MT_SA/data/input/%s/azure/f%s.txt" % (mr, index)
        if os.path.exists(in_path):
            f = open(in_path, 'r')
            if len(f.read()) != 0:
                f.seek(0)
                f.close()
                out_path = "E:/MT_SA/data/output/%s/azure/of%s.txt" % (mr, index)
                sentiment_analysis_example(client, in_path, out_path)
        index += 1
    print("ok")
