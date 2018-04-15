#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from blogsite.wsgi import *
from blog.models import Category,Blog

def main():
    category_urls = [
    ('Django','django'),
    ('Flask','flask'),
    ('爬虫','spider'),
    ]

    for category_name,url in category_urls:
        c = Category.objects.get_or_create(name = category_name,slug = url)[0]

        for i in range(1,11):
            blog = Blog.objects.get_or_create(
                title = '{}_{}'.format(category_name,i),
                slug = 'blog_{}'.format(i),
                content = '新闻详细内容: {} {}'.format(category_name,i)
                )[0]

            blog.category.add(c)

if __name__ == '__main__':
    main()
    print("Done")