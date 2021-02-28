#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name=u'图书名')
    bpub_date = models.DateField(auto_now_add=True, verbose_name=u'发布日期')
    bread = models.IntegerField(default=0, verbose_name=u'阅读量')
    bcomment = models.IntegerField( default=0, verbose_name=u'评论量')
    is_delete = models.BooleanField(default=False, verbose_name=u'删除')

    class Meta:
        verbose_name=u'图书'


class CharacterInfo(models.Model):
    GENDER_CHOICE = (
        (0, 'male'),
        (1, 'female'),
    )
    cname = models.CharField(max_length=20, verbose_name=u'名称')
    cgender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0,
                                       verbose_name=u'性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name=u'人物描述')
    # 一对多，一个书中有多个人物
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE,
                              verbose_name=u'图书', related_name=u'characters')

    class Meta:
        verbose_name = u'人物信息'

