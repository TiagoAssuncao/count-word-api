from django.conf.urls import url
from counter import views

urlpatterns = [
    url(r'^get$', views.get_counter),
    url(r'^', views.counter_list),
]
