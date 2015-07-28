from django.shortcuts import render
from .models import Note
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from notes.forms import NoteForm
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView

# Create your views here.
class NoteList(ListView):
    model = Note

def notes_list(request):
    allnotes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': allnotes})
    
def note(request, pk):
    note = Note.objects.get(id = pk)
    return render(request, 'notes/detail_note.html', {'note_det':note})
    
class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm

class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm
    
class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy("main")