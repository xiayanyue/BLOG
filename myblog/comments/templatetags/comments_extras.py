from django import template
from ..forms import CommentForm
from ..models import Comment
register = template.Library()

@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }

@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    # comment_list = post.comments_set.all().order_by('-created_time')
    comment_list = Comment.objects.filter(post=post).order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }


@register.inclusion_tag('blog/detail.html', takes_context=True)
def show_comments_count(context, post):
    # comment_list = post.comments_set.all().order_by('-created_time')
    comment_list = Comment.objects.filter(post=post).order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,

    }