#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/1/7 16:33
__author__ = 'the king of north'

from django.shortcuts import render


def carlists(request):
    clists = [{"Id": 1, "brand": "11", "name": "ll", "price": 1, "type": 1},
              {"Id": 1, "brand": "11", "name": "ll", "price": 1, "type": 1},
              {"Id": 1, "brand": "11", "name": "ll", "price": 1, "type": 1}]
    return render(request, 'carlist.html', {'carlists': clists})
