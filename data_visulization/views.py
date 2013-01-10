# Create your views here.

from django.views.generic import FormView
from data_visulization.forms import SignupForm, SignupModelForm


class SignupView(FormView):
    '''Sign up View Class '''
    template_name = 'data_visulization/signup.html'
    form_class = SignupForm
    success_url = 'signup/'





	
