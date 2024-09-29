from django.contrib import admin
from news.models import CategoryModel, TagModel, AuthorModel, NewsModel

admin.site.register(CategoryModel)
admin.site.register(TagModel)
admin.site.register(AuthorModel)
admin.site.register(NewsModel)
