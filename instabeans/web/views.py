from django.shortcuts import render_to_response
from .models import Seo
# Create your views here.


def index(request):
    context = dict()
    seo = Seo.objects.all()[0]
    return render_to_response('index.html', {'seo':seo})
