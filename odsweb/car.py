#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/1/7 16:33
__author__ = 'the king of north'

from django.shortcuts import render
from django.core.paginator import Paginator


def carlists(request):
    clists = [{"Id": 1, "brand": "11", "name": "ll", "price": 1, "type": 1},
              {"Id": 1, "brand": "11", "name": "ll", "price": 1, "type": 1},
              {"Id": 1, "brand": "11", "name": "ll", "price": 1, "type": 1}]
    return render(request, 'carlist.html', {'carlists': clists})


def get_article(request):
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    print('PAGE 参数为：', page)
    article_list = [{"article_id": 1, "article_title": "11", "name": "ll", "price": 1, "type": 1},
                    {"article_id": 1, "article_title": "11", "name": "ll", "price": 1, "type": 1},
                    {"article_id": 1, "article_title": "11", "name": "ll", "price": 1, "type": 1}]
    # 实例化一个分页组件，第一个参数是需要被分页的列表，第二个参数是每一个的item个数，比如这边指定每页个数为2
    paginator = Paginator(article_list, 2)
    # page方法，传入一个参数，表示第几页的列表，这边传入的page，是你在地址中写的参数
    page_article_list = paginator.page(page)
    page_num = paginator.num_pages
    # print('page_num:',page_num);
    # 判断是否存在下一页
    if page_article_list.has_next():
        next_page = page + 1

    else:
        next_page = page
    # 是否存在上一页
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page

    return render(request, 'pagetable.html', {
        # 根据前端，我们需要知道当前page的列表，需要知道点击【上一页】，跳转，点击下一页的跳转，需要知道被分了几页
        'article_list': page_article_list,
        'page_num': range(1, page_num + 1),
        'curr_page': page,
        'next_page': next_page,
        'previous_page': previous_page
    })
