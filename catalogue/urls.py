from django.conf.urls import url
from .views import show_data

urlpatterns = [
    url('show_data',show_data)
]