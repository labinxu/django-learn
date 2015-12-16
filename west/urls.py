# -*- coding: utf-8 -*-
from django.conf.urls import url
import west.views

urlpatterns = [
    url('^$', west.views.first_page),
    url('^staff/', west.views.staff),
    url('^templay/', west.views.templay),
    url('^form/', west.views.form),
    url('^investigate/', west.views.investigate),
    url('^investigate_form/', west.views.investigate_form),
]
