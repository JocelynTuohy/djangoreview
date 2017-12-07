from django.conf.urls import url
from . import views

app_name="time_display"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^time_display$', views.index, name="time_display_index")
]