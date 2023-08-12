from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
path('', views.index, name='home'),
path('about', views.about, name='about'),
path('contact', views.contact, name='contact'),
path('vanilla', views.vanilla, name='vanilla'),
path('chocolate', views.chocolate, name='chocolate'),
path('strawberry', views.strawberry, name='strawberry'),
]
