from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes import views
from notes.models import Note

urlpatterns = patterns('',
    url(r'^note/(?P<pk>\d+)/$', views.NoteDetail.as_view(), name = "detail"),
    #url(r'^main/', views.NoteList.as_view(), name='main'),
    url(r'^list/$', views.NoteList.as_view(), name='notes_list'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^add/', views.NoteCreate.as_view(), name='note_add'),
    url(r'^add/$', views.MyView.as_view(), name="note_add"),
    url(r'^note/(?P<pk>\d+)/edit/$', views.NoteUpdate.as_view(),  name='note_update'),
    url(r'^note/(?P<pk>\d+)/delete/$', views.NoteDelete.as_view(), name = "delete_note"),
    url(r'^accounts/', include('accounts.urls')),
)

