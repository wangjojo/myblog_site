from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def index(request):
    home_display_categorys = Category.objects.filter(home_display = True)
    #展示设计为首页展示6条博客，图片廊作用待定
    blogs = Blog.objects.all().order_by('-update_time')[:5]

    return render(request,'index.html',{'home_display_categorys':home_display_categorys,'blogs':blogs})

def category_detail(request,category_slug):
    category = Category.objects.get(slug = category_slug)
    blogs = category.blog_set.all().order_by('-update_time') #查询该栏目下博客数,并按时间排序

    paginator = Paginator(blogs,4)  #按4条1页分

    page = request.GET.get('page')
    #如果page参数存在，则以page的值作为当前页，如果不存在，则视为第1页
    #object_list是数据集，jQuery对象在里面,注意哦
    if page:
        blog_list = paginator.page(page).object_list
    else:
        blog_list = paginator.page(1).object_list

    #判断是否还有前一页和后一页，实现分页功能
    try:
        now_page = paginator.page(page)
    except PageNotAnInteger:
        now_page = paginator.page(1)
    except EmptyPage:
        now_page = paginator.page(paginator.num_pages)

    return render(request,'category_detail.html',{'category':category,'now_page':now_page,'blog_list':blog_list})

def category_detail_all(request):
    #所有博客,想办法优化成一个函数
    blogs = Blog.objects.all().order_by('-update_time') #查询该栏目下博客数,并按时间排序
    paginator = Paginator(blogs,4)  #按4条1页分

    page = request.GET.get('page')
    #如果page参数存在，则以page的值作为当前页，如果不存在，则视为第1页
    #object_list是数据集，jQuery对象在里面,注意哦
    if page:
        blog_list = paginator.page(page).object_list
    else:
        blog_list = paginator.page(1).object_list

    #判断是否还有前一页和后一页，实现分页功能
    try:
        now_page = paginator.page(page)
    except PageNotAnInteger:
        now_page = paginator.page(1)
    except EmptyPage:
        now_page = paginator.page(paginator.num_pages)

    return render(request,'category_detail.html',{'now_page':now_page,'blog_list':blog_list})


def blog_detail(request,pk,blog_slug):
    blog = Blog.objects.get(id = pk)

    if blog_slug != blog.slug:
        return redirect(blog,permanent = True)

    return render(request,'blog_detail.html',{'blog':blog})