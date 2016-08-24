from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("BookDetails", {"fields": ["title","authors"]}),
        ("Review", {"fields": ["is_favourite", "review", "date_reviewed"]}),
        ("Uday Tweak", {"fields": ["title"]}),
    ]
    readonly_fields = ("date_reviewed",)

    def book_authors(self, obj):
        return obj.list_authors()

    book_authors.short_description = "Authors"

    list_display = ["title", "book_authors", "date_reviewed", "is_favourite",]
    list_editable = ["is_favourite"]
    list_display_links = ["title","date_reviewed"]
    list_filter = ["is_favourite"]
    search_fields = ["title","authors__name"]

class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Author fields", {"fields": ["name"]})
    ]

# Register your models here

#admin.site.register(Book, BookAdmin) ----> this is done using a decorator,
                                           # annotation above class "BookAdmin"
admin.site.register(Author, AuthorAdmin)