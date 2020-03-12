from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[\d]+)$', views.UserView.as_view(), name='user'),
]
