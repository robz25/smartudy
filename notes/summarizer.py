# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------


# import env
from django.conf import settings


"""
FILE: sample_extract_summary.py

DESCRIPTION:
    This sample demonstrates how to submit text documents for extractive text summarization.
    Extractive summarization is available as an action type through the begin_analyze_actions API.

USAGE:
    python sample_extract_summary.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_LANGUAGE_ENDPOINT - the endpoint to your Language resource.
    2) AZURE_LANGUAGE_KEY - your Language subscription key
"""


# document needs to be a list
def summarizer(document):
    # [START extract_summary]
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    HOST = settings.HOST1
    KEY = settings.KEY1

    text_analytics_client = TextAnalyticsClient(
        endpoint=HOST,
        credential=AzureKeyCredential(KEY),
    )

    poller = text_analytics_client.begin_extract_summary(document)
    extract_summary_results = poller.result()
    for result in extract_summary_results:
        if result.kind == "ExtractiveSummarization":
            return ("Summary extracted: \n{}".format(
                " ".join([sentence.text for sentence in result.sentences]))
            )
        elif result.is_error is True:
            return ("...Is an error with code '{}' and message '{}'".format(
                result.error.code, result.error.message
            ))
    # [END extract_summary]
