from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index), #위의 urls.py와는 달리 include가 없습니다.
]