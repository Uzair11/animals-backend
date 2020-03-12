from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AnimalListView.as_view(), name='animal_create_view'),
    url(r'^(?P<pk>[\d]+)$', views.AnimalView.as_view(), name='animal_view'),
]
