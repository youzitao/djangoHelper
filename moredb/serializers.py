#!/usr/bin/python
# -*- coding: utf-8 -*-


from rest_framework import serializers
from moredb import models

class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.BookInfo