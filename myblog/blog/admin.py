from django.contrib import admin

# Register your models here.

from .models import Post,Category,Tag

# 在 admin 后台的文章列表页面，我们只看到了文章的标题，但是我们希望它显示更加详细的信息，这需要我们来定制 admin 了
# list_display 属性控制 Post 列表页展示的字段。此外还有一个 fields 属性，则用来控制表单展现的字段
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']
# 将request.user关联到创建的Post实例上，然后将Post数据再保存到数据库
    def save_model(self,request,obj,form,change):
        obj.author = request.user
        super().save_model(request,obj,form,change)


#注册后台管理用户
# 把新增的 Postadmin 也注册进来
admin.site.register(Post,PostAdmin)

admin.site.register(Category)
admin.site.register(Tag)





