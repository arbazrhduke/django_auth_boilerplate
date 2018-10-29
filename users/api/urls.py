from django.conf.urls import url
from .views import LoginAPIView


urlpatterns = [
    url(r'^login$', LoginAPIView.as_view()),
]