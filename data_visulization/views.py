# Create your views here.

from django.views.generic import FormView, View, TemplateView
from data_visulization.forms import SignupForm, LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class SignupView(FormView):
    '''Sign up View Class '''
    template_name = 'data_visulization/signup.html'
    form_class = SignupForm
    success_url = 'signup/'




class LoginView(TemplateView):
	form = LoginForm
	template_name = 'data_visulization/login.html'

	def get_context_data(self, **kwargs):

		if 'form' not in kwargs:
			kwargs['form'] = LoginForm()

		return kwargs

	def post(self, request, *args, **kwargs):
		#do application logic right here
		#process form logic
		form = self.form(request.POST)

		if form.is_valid():			

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				#redirect to a new place
			else:
				HttpResponse('You are not a user!!')
		else:

			return self.render_to_response(self.get_context_data(form=form))

		return HttpResponse(request.user)




class HomeRedirectView(View):
 	''' will check to see if login cookie is set, and then redirect to correct page '''

 	def get(self, request, *args, **kwargs):
 		pass


class DashBoardView(TemplateView):
	#grab session of user
	pass




	
