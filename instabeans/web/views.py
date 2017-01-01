from django.shortcuts import render_to_response,render
from django.template import RequestContext
from .models import Testimonial, Project
from .form import ContactForm
from django.contrib import messages
# Create your views here.


def index(request):
    context = {}
    context['index'] = True
    context['testimonials'] = Testimonial.objects.all()
    context['projects'] = Project.objects.all()[:3]
    return render_to_response('index2.html', context)


def work(request):
    context = {}
    context['work'] = True
    context['projects'] = Project.objects.all()
    return render_to_response('work.html', context)


def contact(request):
    context = {}
    context['contact'] = True
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Form Submitted')
    return render(request, 'contact.html', context)

def handler404(request):
    response = render(request, '404.html')
    response.status_code = 404
    return response
