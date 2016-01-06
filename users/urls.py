# -*- coding: utf-8 -*-
from django.conf.urls import url
import users.views

urlpatterns = [
    url('^login/', users.views.user_login),
    url('^logout/', users.views.user_logout),
]
