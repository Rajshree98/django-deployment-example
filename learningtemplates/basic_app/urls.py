from django.conf.urls import url
from basic_app import views

app_name='basic_app'

urlpatterns=[
            url('others/',views.others,name='others'),
            url('relative/',views.relative,name='relative')
]