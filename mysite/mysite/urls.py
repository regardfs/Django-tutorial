"""mysite URL Configuration

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
from Parkson.views import helloworld, math, PizzaHut, menu, restaurants_list, menu1, menu2, restaurants_list1, comment
from Parkson.views import comment_as_table
from mysite.views import welcome

# django will automatically add '/' before admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^helloworld/$', helloworld),
    url(r'^(\d{1,3})/math/(\d{1,3})/$', math),   #(\d{1,2,3}) means from 0 to 999
    url(r'^PizzaHut/$', PizzaHut),
    url(r'^menu/$', menu),
    url(r'^menu1/(\d{1,5})/$', menu1),
    url(r'^welcome/$', welcome),
    url(r'^restaurants_list/$', restaurants_list),
    url(r'^restaurants_list1/$', restaurants_list1),
    url(r'^menu2/(\d{1,5})/$', menu2),
    url(r'^comment/(\d{1,5})/$', comment),
    url(r'^comment_as_table/(\d{1,5})/$', comment_as_table),
]

