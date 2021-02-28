#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import viewsets
from moredb.serializers import BookInfoSerializer, CharacterInfoSerializer
from moredb.models import BookInfo,CharacterInfo
from rest_framework import generics


class BookInfoView(viewsets.ModelViewSet):
# class BookInfoView(generics.ListAPIView):# 不支持路由中base_name方式

    serializer_class = BookInfoSerializer
    def get_queryset(self):
        '''
        没有queryset属性重写此方法需要在路由注册中指定base_name
        :return:
        '''
        condtions = {}
        for qur_name, qur_value in self.request.query_params.items():
            condtions[qur_name]=qur_value[0] if qur_value and isinstance(
                qur_value, list) else qur_value

        queryset = BookInfo.objects.filter(**condtions)
        return queryset

class CharacterInfoView(viewsets.ModelViewSet):

    serializer_class = CharacterInfoSerializer
    def get_queryset(self):
        '''
        没有queryset属性重写此方法需要在路由注册中指定base_name
        :return:
        '''
        condtions = {}
        for qur_name, qur_value in self.request.query_params.items():
            condtions[qur_name]=qur_value[0] if qur_value and isinstance(
                qur_value, list) else qur_value

        queryset = CharacterInfo.objects.filter(**condtions)
        return queryset
