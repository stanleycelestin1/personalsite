
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.utils import timezone
from django.core.mail import send_mail, BadHeaderError

from django.template import loader

# class IndexView(generic.DetailView):
#     template_name = 'personalsite/index.html'

def index(request):
	return render(request, 'personalsite/index.html')
 



 



