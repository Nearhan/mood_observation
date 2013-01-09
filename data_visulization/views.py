# Create your views here.

from django.views.generic import FormView


class SignupView(FormView):
	template_name = 'data_visulization/signup.html'

	
