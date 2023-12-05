import sqlite3
# import env
from django.conf import settings

import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig


KEY = settings.KEY1
REGION = settings.REGION1


# Functions necesaries to Insert audio to sqlite3
def to_binary(filename):
    '''Convert data to binary format'''
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def insert_blob(name, audio):
    try:
        sqlite_connection = sqlite3.connect('audio.db')
        cursor = sqlite_connection.cursor()
        print("Connected to SQLite")
        sqlite_query = "INSERT INTO audio_table (name, audio) VALUES (?, ?)"
        emp_audio = to_binary(audio)
        ##resume = to_binary(resume_file)
        # Convert data into tuple format
        data_tuple = (name, emp_audio)
        cursor.execute(sqlite_query, data_tuple)
        sqlite_connection.commit()
        print("File inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print(f"Failed to insert blob data into sqlite table {error}")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("The sqlite connection is closed")
 



##Main function with strings input

def speaker(text_input, name):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=KEY, region=REGION)
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3)
    file_name = name+".mp3"
    file_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)
     # Receives a text from console input and synthesizes it to mp3 file.
    text = text_input;
    result = speech_synthesizer.speak_text_async(text).get()
            # Check result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}], and the audio was saved to [{}]".format(text, file_name))
        insert_blob(name,name+".mp3")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

""" def speaker(name,)
        #from datetime import datetime
        #from uuid import uuid4
        #eventid = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
        insert_blob("test", "outputaudio.mp3") """
