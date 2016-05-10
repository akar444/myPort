from django.conf.urls import url
from . import views

app_name = 'myPort'

urlpatterns = [
    url(r'^airports/$',views.airpot_list,name="airports-list"),
]