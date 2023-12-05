import os
from dotenv import load_dotenv
import time
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

# import env
from django.conf import settings

# Import namespaces

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

global cv_client

try:
    # Get Configuration Settings
    load_dotenv()
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    HOST = settings.HOST1
    KEY = settings.KEY1

    # Authenticate Azure AI Vision client
    credential = CognitiveServicesCredentials(KEY)
    cv_client = ComputerVisionClient(HOST, credential)

except Exception as ex:
    print(ex)


def GetTextRead(image_file):
    output = ""
    print('Reading text in {}\n'.format(image_file))
    # Use Read API to read text in image
    # with open(image_file, mode="rb") as image_data:
    with image_file.docfile.open('rb') as image_data:
        read_op = cv_client.read_in_stream(image_data, raw=True)
    # Get the async operation ID so we can check for the results
        operation_location = read_op.headers["Operation-Location"]
        operation_id = operation_location.split("/")[-1]
# Wait for the asynchronous operation to complete
    while True:
        read_results = cv_client.get_read_result(operation_id)
        if read_results.status not in [OperationStatusCodes.running, OperationStatusCodes.not_started]:
            break
        time.sleep(1)
# If the operation was successfully, process the text line by line
    if read_results.status == OperationStatusCodes.succeeded:
        for page in read_results.analyze_result.read_results:
            for line in page.lines:
                print(line.text)
                # Uncomment the following line if you'd like to see the bounding box
                # print(line.bounding_box)
                output += line.text
                # Uncomment the following line if you'd like to see the bounding box
                # print(line.bounding_box)
    return output
