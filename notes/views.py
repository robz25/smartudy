from typing import List
from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.http import FileResponse
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from .forms import NotesForm
from .models import Notes
from .models import get_audio_file
from .models import Audio



# upload file
from .models import Document
from .forms import DocumentForm

# ocr
from .ocr import GetTextRead

# summarize text
from .summarizer import summarizer

global cv_client


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"


class ServeAudio(View):
    def get(self, request, *args, **kwargs):
        audio_name = kwargs['audio_name']
        sql_path = 'audio.db'
        audio_data = get_audio_file(sql_path, audio_name)
        return HttpResponse(audio_data, content_type='audio/mpeg')


# upload file
def upload_file(request):
    message = ''
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            newdoc = Document(docfile=request.FILES['docfile'], title=title)
            newdoc.save()
            # extracted_text = GetTextRead(newdoc)
            # print(extracted_text)

            # Redirect to the document list after POST
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'notes/upload.html', context)


def delete_document(request, document_id):
    Document.objects.filter(id=document_id).delete()
    return redirect('my-view')  # here goes the view NAME of the url file


def extract_text_with_ocr(request, document_id):
    document_path = Document.objects.filter(id=document_id)
    document_path = Document.objects.get(id=document_id)
    document_title = document_path.title
    print("docu title ", document_title)
    print(Document.objects)

    # print(dir(document_path))
    text_from_file = GetTextRead(document_path)
    summarized_text = summarizer([text_from_file])
    note = Notes(title=document_title, text=text_from_file, summarized_text=summarized_text)
    note.save()
    print("summarized_text: ", summarized_text)
    messages.info(request, 'Note successfully generated')
    return redirect('my-view')
