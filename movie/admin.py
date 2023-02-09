from django.contrib import admin
from .models import Movie, CategoryNews, News, Settings, Contact


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title', )}
    list_display = ['title', 'genre']


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title', )}
    list_display = ['title', 'draft']


admin.site.register(Contact)
admin.site.register(Settings)
admin.site.register(CategoryNews)
admin.site.register(News, NewsAdmin)
admin.site.register(Movie, MovieAdmin)
