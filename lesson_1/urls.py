from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lesson_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^note/(?P<note_id>\d+)/$', views.note, name = "detail"),
    url(r'^main/', views.notes_list, name = "notes_list"),
    url(r'^admin/', include(admin.site.urls)),
)
