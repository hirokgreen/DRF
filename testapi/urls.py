"""testapi urls"""
from django.conf.urls import url
from testapi import views

urlpatterns = [
    url(r'^api/v1/contact/$', views.contact_details, name='contact_details'),
    url(r'^api/v1/contact/(?P<primary_key>[0-9]+)$', views.contact_element, name='contact_element')
]

