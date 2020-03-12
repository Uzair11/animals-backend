from django.conf.urls import url, include
from api.authentication import urls as auth_urls
from api.user import urls as user_urls
from api.animal import urls as animal_urls

urlpatterns = [
    url(r'^auth/', include(auth_urls)),
    url(r'^user/', include(user_urls)),
    url(r'^animal/', include(animal_urls)),
]
