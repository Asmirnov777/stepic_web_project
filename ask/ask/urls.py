"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from qa.views import test

urlpatterns = [
    ##path('admin/', admin.site.urls),
    #path('', test),
    #path('question/<int:question_id>/', test),
    #path('login/', test),
    #path('signup/', test),
    #path('ask/', test),
    #path('popular/', test),
    #path('new/', test)
    url(r'^$', test, name='index_func'),
    url(r'^login/$', test, name='login_func'),
    url(r'^signup/$', test, name='signup_func'),
    url(r'^question/(?P<id>[^/]+)/$', test, name='test'),
    url(r'^ask/$', test, name='ask_func'),
    url(r'^popular/$', test, name='popular_func'),
    url(r'^new/$', test, name='new_func')
]
