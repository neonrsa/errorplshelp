from django.contrib import admin
from .models import Note, Folder, Tag
# Register your models here.
from accounts.models import UserProfile

class NoteInline(admin.StackedInline): #Demo StackedInline vs TabularInline
    model = Note
    fields = ('title',) 
    extra = 0
    
class FolderAdmin(admin.ModelAdmin):
    inlines = [NoteInline,]
    
    model = Folder


#http://stackoverflow.com/questions/6479999/django-admin-manytomany-inline-has-no-foreignkey-to-error    
#https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-models
class TaggedNoteInline(admin.TabularInline): 
    model = Note.tag.through
    extra = 0
    
class TagAdmin(admin.ModelAdmin):
    inlines = [TaggedNoteInline,]
    model = Tag
    

admin.site.register(Note)
admin.site.register(Folder)
admin.site.register(Tag)
admin.site.register(UserProfile)