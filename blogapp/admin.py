from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')  # Postlar ruyxati ko'rinadi
    list_filter = ('status', 'created', 'publish', 'author')  # filterlash
    search_fields = ('title', 'body')  # qidirish uchun
    prepopulated_fields = {'slug':('title',)}  # title ga qarab o'zi yaratadi
    raw_id_fields = ('author',) # admin panelda ko'rinadi
    date_hierarchy = 'publish' # ro'yxatni ko'rsatilish tartibi
    ordering = ('status', 'publish') # status publish bo'lganlar yuqorida turishi uchun
