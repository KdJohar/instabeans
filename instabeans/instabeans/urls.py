"""instabeans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from web import views as web_views
from django.conf import settings
from django.conf.urls import (
    handler404, handler500
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', web_views.index, name='index'),
    url(r'^work/$', web_views.work, name='work'),
    url(r'^contact/$', web_views.contact, name='contact'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = web_views.handler404
handler500 = web_views.handler404