from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes import views
from notes.models import Note

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lesson_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^note/(?P<pk>\d+)/$', views.note, name = "detail"),
    #url(r'^main/', views.notes_list, name = "notes_list"),
    url(r'^main/', views.NoteList.as_view(model = Note), name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/', views.NoteCreate.as_view(), name='note_add'),
    url(r'^note/(?P<pk>\d+)/edit/$', views.NoteUpdate.as_view(),  name='note_update'),
    url(r'^note/(?P<pk>\d+)/delete/$', views.NoteDelete.as_view(), name = "delete_note"),
)
