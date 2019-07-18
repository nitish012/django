from django.urls import path
from quickstart import views


urlpatterns=[
    path('',views.index,name='index')
]