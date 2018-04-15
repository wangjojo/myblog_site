# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse
 
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField('分类名称', max_length=30)
    slug = models.CharField('分类网址', max_length=256, db_index=True)
    intro = models.CharField('分类简介', max_length = 200)

    home_display = models.BooleanField('导航显示', default=True)

    def get_absolute_url(self):
        return reverse('category',args=(self.slug,))

    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['name']  # 按照哪个栏目排序
 
 
@python_2_unicode_compatible
class Blog(models.Model):
    category = models.ManyToManyField(Category, verbose_name='归属分类')
 
    title = models.CharField('标题', max_length=30)
    slug = models.CharField('网址', max_length=256, db_index=True)
 
    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
    content = UEditorField('内容', height=300, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
 
    published = models.BooleanField('正式发布', default=True)

    pub_date = models.DateTimeField('发布时间',auto_now_add = True,editable = True)
    update_time = models.DateTimeField('更新时间',auto_now = True,null = True)
 
    def get_absolute_url(self):
        return reverse('blog',args=(self.id,self.slug))

    def __str__(self):
        return self.title
 
    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name