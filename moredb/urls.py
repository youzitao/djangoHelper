#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from moredb import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# basename 创建url的名字，默认是viewset的queryset，
# 所以如果viewset类中没用queryset属性，必须设置basename
router.register(r'bookinfo', views.BookInfoView, base_name='BookInfo')
router.register(r'characterinfo', views.CharacterInfoView, base_name='CharacterInfo')

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]