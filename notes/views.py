from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from notes.forms import NoteForm
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import UserProfile
from .models import Note, Folder, Tag
from .forms import NoteForm, FolderForm, TagForm
from django.core.serializers.json import DjangoJSONEncoder



# Create your views here.


"""def notes_list(request):
    allnotes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': allnotes})
    
def note(request, pk):
    note = Note.objects.get(id = pk)
    return render(request, 'notes/detail_note.html', {'note_det':note})"""
    
class NoteList(ListView):
    model = Note
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoteList, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
        #self.request.user will contain the "User" object, however,
        #user field in the Note model is an instance of "UserProfile" object
        #So need to ensure that when we filter all the user owned notes, we
        #filter using the 'correct' UserProfile instance based on logged in "User" object 
        #in self.request.user
        curruser = UserProfile.objects.get(user=self.request.user)
        folder = self.kwargs['folder']
        if folder == '':
            #filter based on current logged in user
            self.queryset = Note.objects.filter(user=curruser)
            return self.queryset
        else:
            #filter based on current logged in user
            self.queryset = Note.objects.all().filter(user=curruser).filter(folder__title__iexact=folder)
            return self.queryset
    
    
    def get_context_data(self, **kwargs):
        context = super(NoteList, self).get_context_data(**kwargs)
        context['total'] = self.queryset.count()
        #provided so that the avatar can be displayed in base.html
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

    
class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm

class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm
    @method_decorator(login_required)
    
    def dispatch(self, *args, **kwargs):
        return super(NoteUpdate, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(NoteUpdate, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context


    
class NoteDetail(DetailView):
    model = Note
    #@method_decorator(login_required)
    
    def dispatch(self, *args, **kwargs):
        return super(NoteDetail, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(NoteDetail, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context


    
class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy("main")
        
    @method_decorator(login_required)
    
    def dispatch(self, *args, **kwargs):
        return super(NoteDelete, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(NoteDelete, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

class MyView(TemplateView):
    folder_form_class = FolderForm
    tag_form_class = TagForm
    note_form_class = NoteForm
    template_name = "notes/note_hybrid.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyView, self).dispatch(*args, **kwargs)
        
    def get(self, request, *args, **kwargs):
        kwargs.setdefault("createfolder_form", self.folder_form_class())
        kwargs.setdefault("createtag_form", self.tag_form_class())
        kwargs.setdefault("createnote_form", self.note_form_class())
        #Added curruser so that profile picture of curruser can be rendered.
        kwargs.setdefault('curruser', UserProfile.objects.get(user=self.request.user))
        return super(MyView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form_args = {
            'data': self.request.POST,
        }
        
        print("in here haha")
        if "btn_createfolder" in request.POST['form']:
            form = self.folder_form_class(**form_args)
            if not form.is_valid():
                return self.get(request,
                                   createfolder_form=form)
            else:
                form.save()
                data = Folder.objects.all()
                result_list = list(data.values('id','title'))
                return HttpResponse(json.dumps(result_list, cls=DjangoJSONEncoder))
        elif "btn_createtag" in request.POST['form']:
            form = self.tag_form_class(**form_args)
            if not form.is_valid():
                return self.get(request, createtag_form=form)
            else:
                form.save() #save the new object
                data = Tag.objects.all() # retrieve all records
                result_list = list(data.values('id','title'))
                return HttpResponse(json.dumps(result_list, cls=DjangoJSONEncoder)) #return to ajax as success with all the new records.
        elif "btn_createnote" in request.POST['form']:
            print("jjj")
            form = self.note_form_class(**form_args)
            if not form.is_valid():
                print("form not valid")
                return self.get(request, createnote_form=form) 
            else:
                try:
                    #Find out which user is logged in and get the correct UserProfile record.
                    curruser = UserProfile.objects.get(user=self.request.user)
                    obj = form.save(commit=False)
                    obj.user = curruser #Save the note note under that user
                    obj.save() #save the new object
                    
                except Exception, e:
                    print("errors" + str(e))
                response = {'status': 1, 'message':'ok'}
                return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder)) #return to ajax as success with all the new records.
            
        return super(MyView, self).get(request)

