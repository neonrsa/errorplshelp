from django.shortcuts import render
from .models import Note
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

def notes_list(request):
    allnotes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': allnotes})
    
def note(request, note_id):
    note = Note.objects.get(id = note_id)
    resptext = ""
    resptext += "<a href = '/main/' style = 'text-decoration:none'><h1 style='color:gray; font-family:serif; font-size:50pt; text-decoration:none' >IntoTheDeep</h1></a><div style='background-color:black; width:750px; height:auto; padding:25px 25px 40px; display:block'>"
    resptext += "<h2  style='color:white; font-family:serif'>" + note.title + "</h2>"
    resptext += "<p style='color:white; font-family:serif'>"+ note.content + "</p></div>"
    return HttpResponse(resptext)
    