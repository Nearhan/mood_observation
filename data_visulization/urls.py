from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from data_visulization.views import SignupView


urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view()), 
	url(r'^signup/$', SignupView.as_view()))