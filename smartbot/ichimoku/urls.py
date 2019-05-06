from django.urls import path, re_path


from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.test, name='test'),
    #re_path('^(?P<pk>\d+)/$', views.BookDetail.as_view(), name='book-detail'),
    #re_path('^mine/$', views.UsersBooks.as_view(), name='user-books')
]