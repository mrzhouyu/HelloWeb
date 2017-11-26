from django.contrib import admin
from web01.models import Post
# Register your models here.

#增加点别的小标题
class Myadmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

#注册
admin.site.register(Post,Myadmin    )


