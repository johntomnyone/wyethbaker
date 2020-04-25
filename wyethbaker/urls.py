from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from bakerapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^bakerapp/',include('bakerapp.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^email/$', views.email, name='email'),
]