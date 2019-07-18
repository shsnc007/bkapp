# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'wuzhiweitest01.views',
    # 普通任务也没
    (r'^$', 'index'),
)
