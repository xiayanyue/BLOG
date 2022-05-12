from django.shortcuts import render
import markdown
import re
# Create your views here.

# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("欢迎来到夏言悦的博客首页")

# def index(request):
#
#     return render(request,"blog/index.html",context={'title':'我的博客首页','welcome':'欢迎访问我的博客首页'})
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from .models import Post

from comments.models import Comment

from django.shortcuts import get_object_or_404
def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    print("11111")
    print(post_list)

    # 获取每篇文章的所有评论数 组成二维列表传入 模板进行渲染
    #
    # list1= []
    # for post in post_list:
    #     # print("22222")
    #     print(post)
    #     c = Comment.objects.filter(post=post).count()
    #     list1.append([post,c])
    # post_list = list1
    # print(post_list)
    return render(request,"blog/index.html",context={"post_list":post_list})


def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)

    # 阅读量 +1
    post.increase_views()
    # print("+++++++++++")
    # print(post)
    # 安装了markdown 在此视图中解析markdown
    md = markdown.Markdown(extensions=['markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                       # 记得在顶部引入 TocExtension 和 slugify
                                       TocExtension(slugify=slugify),
                                       ])

    post.body = md.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    comment_count = Comment.objects.filter(post=post).count()

    return render(request,"blog/detail.html",context={"post":post,"comment_count":comment_count})

def archive(request,year,month):
    post_list = Post.objects.filter(created_time__year = year,created_time__month = month).order_by("-created_time")
    return render(request,"blog/index.html",context={"post_list":post_list})

#引入Category 类
from .models import Category,Post,Tag

def category(request,pk):
    #记得在开始部分导入Category 类   分类
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    print("66999")
    print(post_list)
    return render(request,"blog/index.html",context={"post_list":post_list})


def tag(request, pk):
    # 记得在开始部分导入 Tag 类   标签
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})





