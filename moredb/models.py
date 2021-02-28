#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name=u'图书名')
    bpub_date = models.DateField(auto_now_add=True, verbose_name=u'发布日期')
    bread = models.IntegerField(default=0, verbose_name=u'阅读量')
    bcomment = models.IntegerField( default=0, verbose_name=u'评论量')
    is_delete = models.BooleanField(default=False, verbose_name=u'逻辑删除')

    class Meta:
        verbose_name=u'图书信息'



