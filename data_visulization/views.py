# Create your views here.

from django.views.generic import FormView, View, TemplateView, ListView
from data_visulization.forms import SignupForm, LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from data_collection.models import Observation

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

		return HttpResponseRedirect(reverse('dashboard'))




class HomeRedirectView(View):
 	''' will check to see if login cookie is set, and then redirect to correct page '''

 	def get(self, request, *args, **kwargs):
 		pass

'''
class DashBoardView(TemplateView):

	template_name= 'data_visulization/dashboard.html'


	def get(self, request, *args, **kwargs):
		return HttpResponse(str(request))


	def get_context_data(self, **kwargs):
		user = self.request.user
		observations = Observation.objects.all().filter(user=user)
		kwargs['observations'] = observations
		kwargs['s'] = 'this is a test string'
		return kwargs
'''

class DashBoardView(ListView):

	model = Observation
	template_name = 'data_visulization/dashboard.html'
	context_object_name = 'observations'
	

	def get_queryset(self):
	    """
	    Get the list of items for this view. This must be an interable, and may
	    be a queryset (in which qs-specific behavior will be enabled).
	    """
	    
	    self.queryset = self.model._default_manager.all().filter(user=self.request.user).order_by('-date')
	    return super(DashBoardView, self).get_queryset()



 
	
