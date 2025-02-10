from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Bgbuild, Bgcomment, Bgreply


@admin.register(Bgbuild)
class BgbuildAdmin(SummernoteModelAdmin):
    list_display = ('bgbuild_title', 'slug', 'status', 'created_on')
    search_fields = ['bgbuild_title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('bgbuild_title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Bgcomment)
admin.site.register(Bgreply)
