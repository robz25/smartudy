from django.urls import path
# from .views import my_view

from . import views
from .views import ServeAudio

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
    path('audio/<str:audio_name>', ServeAudio.as_view(), name='serve_audio'),
    path('delete-document/<int:document_id>/', views.delete_document, name='delete_document'),
    path('get_text/<int:document_id>/', views.extract_text_with_ocr, name='get_text_from_file'),
    path('notes/upload', views.upload_file, name='my-view')
]
