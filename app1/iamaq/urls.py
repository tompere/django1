__author__ = 'mediaserver'

from django.conf.urls import patterns, url

from iamaq import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<q_num>\d+)/$', views.index),
    url(r'^(?P<q_id>\d+)/question/$', views.questionDetails),
)