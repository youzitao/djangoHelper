#!/usr/bin/python
# -*- coding: utf-8 -*-


from rest_framework import serializers
from moredb import models

class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.BookInfo

class BookRelateField(serializers.RelatedField):
    # 自定义类型
    def to_representation(self, value):
        return "Book: %d %s"%(value.id, value.bread)

class CharacterInfoSerializer(serializers.ModelSerializer):
    bookname=serializers.ReadOnlyField(source='hbook.btitle')
    # 利用to_representation方法，自定义一个类，
    # 让hbook外键关联字段称为这个自定义类的实例对象，
    # 注意括号里read_only = True千万别忘了，是个只读字段，
    hbook=BookRelateField(read_only=True)
    class Meta:
        fields = '__all__'
        model = models.CharacterInfo