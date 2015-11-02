

from django.contrib import admin
from books.models import Books
admin.autodiscover()

admin.site.register(Books)