from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.getListBlogDefault),
    re_path(
        r'^sort=(?P<typeSort>[-\s\S]+|())&page_id=(?P<pageNumber>[\d]+|())/$', views.getListBlog_WithNumberPage),
    re_path(
        r'^search=(?P<title>[-\s\S]+|())&page_id=(?P<pageNumber>[\d]+|())/$', views.searchBlogWithTitle),
    path('<str:urlBlog>', views.getBlogByURL),
    path('<str:urlBlogNeedEdit>/chinh-sua/', views.editBlog),
    path('xuat-ban/', views.postBlog)
]
