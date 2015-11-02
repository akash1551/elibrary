

from django.conf.urls import patterns,include,url

urlpatterns = patterns('',
                       url(r'^all/','books.views.books'),
                       #url(r'^json_data/','books.views.book_date'),
                       url(r'^get/(?P<book_id>\d+)/','books.views.get_book'),
                       url(r'^book_data/','books.views.book_data'),
                       url(r'^uploadbook/$','books.views.upload_book'),
                       url(r'^uploadauth/$','books.views.upload_auth'),
                       url(r'^/books/get_upload_file_name/$','books.models.get_upload_file_name'),
                       url(r'^create/$','books.views.upload_auth'),
                       url(r'^newbook/$','books.views.new_book'),
                       url(r'^search/$','books.views.search_titles'),
                       url(r'^save_data/$','books.views.save_data'),

                       #url(r'^viewbooks/$','books.views.view_books'),
                       #url(r'^viewvideos/$','books.views.view_videos'),

                       )
