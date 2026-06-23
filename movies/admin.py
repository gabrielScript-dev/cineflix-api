from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ('id', 'title')
    search_fields = ('title',)
