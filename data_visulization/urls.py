from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from data_visulization.views import SignupView, HomeRedirectView, LoginView, DashBoardView


urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view()),
	url(r'^login/$', LoginView.as_view()),  
	url(r'^signup/$', SignupView.as_view()),
	url(r'^dashboard/$', DashBoardView.as_view()))
