# -*- coding: utf-8 -*-
from django.conf.urls import url
import west.views

urlpatterns = [
    url('^$', west.views.first_page),
    url('^staff/', west.views.staff)
]
