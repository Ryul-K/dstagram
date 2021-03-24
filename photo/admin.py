from django.contrib import admin

# Register your models here.
from .models import Photo
class PhotoAdmin(admin.ModelAdmin): #이름은 마음대로 강사는 [AppName]Admin으로함
    list_display = ['id', 'author', 'created', 'updated']
    raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text','created', 'author__username']
    #foreignkey 하위 username불러와라~
    ordering = ['-updated', '-created'] #'-'내림차순, 관리자페이지에서의 정렬
    #admin 커스터마이징하는 옵션 많음 list_xxxx
admin.site.register(Photo, PhotoAdmin)