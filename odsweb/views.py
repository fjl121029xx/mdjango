#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/1/7 15:51
__author__ = 'the king of north'

from django.shortcuts import render


# python manage.py runserver 0.0.0.0:8001


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)


def runoob2(request):
    context = {}
    context['hello'] = 'Hello Worl2d!++'
    return render(request, 'runoob2.html', context)


def runoob_list(request):
    views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    return render(request, "runoob2.html", {"views_list": views_list})
