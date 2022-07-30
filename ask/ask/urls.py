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
from qa.views import test, question_view, popular_view, new_view, question_add, login_view, signup_view
#import qa.views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', test),
    path('', new_view, name='new-view'),
    path('popular/', popular_view, name='popular-view'),
    path('question/<int:id>/', question_view, name='question-view'),
    path('login/', login_view, name='login-view'),
    path('signup/', signup_view, name='signup_view'),
    path('ask/', question_add, name='question-add')
    #path('new/', new_view, name='new-view')

    #url(r'login/', test, name='login_func'),
    #url(r'signup/', test, name='signup_func'),
    #url(r'question/(?P<id>[^/]+)/', question_view, name='question-view'),
    #url(r'ask/', question_add, name='question-add'),
    #url(r'popular/', popular_view, name='popular-view'),
    #url(r'', new_view, name='new-view')
]
