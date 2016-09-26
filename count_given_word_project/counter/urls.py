from django.conf.urls import url
from counter import views

urlpatterns = [
    url(r'^counters/$', views.counter_list),
    url(r'^get_counter$', views.get_counter),
]
