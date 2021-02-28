#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import viewsets
from moredb.serializers import BookInfoSerializer
from moredb.models import BookInfo
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

# class PurchaseList(generics.ListAPIView):
#     serializer_class = PurchaseSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return Purchase.objects.filter(purchaser=user)