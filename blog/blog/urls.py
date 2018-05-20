"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from xujia import views as xj_views
from xujia.controllers.roast import views as roast_views
from xujia.controllers.article import views as article_views

urlpatterns = [
    url(r'^register$', xj_views.register, name='register'),
    url(r'^login$', xj_views.login, name='login'),
    url(r'^logout$', xj_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^roast/index$', roast_views.index, name='roast_index'),
    url(r'^roast/api_talk', roast_views.api_talk, name='api_talk'),
    url(r'^roast/api_get_list', roast_views.api_get_list, name='api_get_list'),
    url(r'^article/index$', article_views.index, name='article_index'),
    url(r'^article/publish', article_views.publish, name='article_publish'),
    url(r'^$', xj_views.index, name='index'),
]
