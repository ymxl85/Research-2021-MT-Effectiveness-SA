"""
    document_sentiment
"""

key = "f917b7f7fec848f5b94f926c34f7dea3"
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
        string += line.strip()
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
    index = 1810
    case_num = 2000
    mr = "mr6_2/azure"
    while index <= case_num:
        f_index = 1
        while f_index <= 10:
            f_path = "E:/MT_SA/data/input/%s/f%s_%s.txt" % (mr, index, f_index)
            if os.path.exists(f_path):
                of_path = "E:/MT_SA/data/output/%s/of%s_%s.txt" % (mr, index, f_index)
                sentiment_analysis_example(client, f_path, of_path)
            f_index += 1
        index += 1
    print("ok")
