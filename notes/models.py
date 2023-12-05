from django.db import models
from .summarizer import summarizer
from .speaker import speaker
import pathlib
import sqlite3

# ocr
from .ocr import GetTextRead


class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    summarized_text = models.TextField(default='SOME STRING')

    def save(self, *args, **kwargs):
        self.summarized_text = summarizer([self.text])
        super(Notes, self).save(*args, **kwargs)
        speaker(self.summarized_text, self.title)
        file_to_rem = pathlib.Path(self.title+".mp3")
        file_to_rem.unlink()
        print("file saved db, removed enviroment")


""" 
def get_audio_file(db_path, audio_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT audio_data FROM audio_table WHERE id=?", (audio_id,))
    audio_data = cursor.fetchone()[0]
    conn.close()
    return audio_data """

""" 
class Audio(models.Model):
    audio_file = models.FileField(upload_to='audios/')
Audio.objects=Audio.objects.using('audio') """


def get_audio_file(db_path, audio_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT audio FROM audio_table WHERE name=?", (audio_name,))
    audio = cursor.fetchone()[0]
    conn.close()
    return audio


class Audio(models.Model):
    name = models.AutoField(primary_key=True)
    audio_data = models.BinaryField()


""" def get_audio_file(audio_name):
    audio = Audio.objects.using("audio").get(name=audio_name)
    return audio.audio_data """


class Document(models.Model):
    path_to_save = 'documents/%Y/%m/%d'
    title = models.CharField(max_length=255, default="No title provided")
    docfile = models.FileField(upload_to=path_to_save)

    # def save(self, *args, **kwargs):
        # extracted_text = GetTextRead(self.docfile.name)
        # print(extracted_text)
        #super(Notes, self).save(*args, **kwargs)

