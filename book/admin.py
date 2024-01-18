from django.contrib import admin

from book.models import Book, Comment

# admin.site.register(Book)
admin.site.register(Comment)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
