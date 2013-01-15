from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from data_visulization.views import SignupView, HomeRedirectView, LoginView, DashBoardView
from django.contrib.auth.decorators import login_required, permission_required


urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view()),
	url(r'^login/$', LoginView.as_view()),  
	url(r'^signup/$', SignupView.as_view()),
	url(r'^dashboard/$', login_required(DashBoardView.as_view()), name='dashboard'))
