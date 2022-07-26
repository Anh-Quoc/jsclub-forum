from django.shortcuts import render
from .forms import BlogForm
from .models import Blog
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from .inputProcess import *


def getListBlogDefault(request):
    return HttpResponseRedirect(URL_GET_LIST_BLOG_DEFAULT)


def getListBlogWithPagination(queryBlog, pageNumber):
    paginator_page = Paginator(queryBlog, NUMBER_BLOG_IN_ONE_PAGE)
    pageNumber = int(pageNumber)
    if pageNumber > paginator_page.num_pages:
        pageNumber = paginator_page.num_pages

    try:
        page_obj = paginator_page.get_page(pageNumber)
        indexPage = pageNumber
    except PageNotAnInteger:
        page_obj = paginator_page.get_page(1)
        indexPage = 1
    except EmptyPage:
        page_obj = paginator_page.page(paginator_page.num_pages)
        indexPage = paginator_page.num_pages

    data = {'page_obj': page_obj,
            'totalPages': paginator_page.num_pages,
            'indexPage': indexPage,
            'status': 'Found'}

    return data


def getListBlog_WithNumberPage(request, typeSort, pageNumber):
    queryBlog = Blog.objects.filter(
        status=DIC_BLOG_STATUS['STATUS_Approve']).order_by('-dateTime')
    if request.method == 'GET':
        if typeSort == TYPE_SORT_BLOG[0]:
            queryBlog = Blog.objects.filter(
                status=DIC_BLOG_STATUS['STATUS_Approve']).order_by('-dateTime')
        elif typeSort == TYPE_SORT_BLOG[1]:
            queryBlog = Blog.objects.filter(
                status=DIC_BLOG_STATUS['STATUS_Approve']).order_by('-countViewer')
        else:
            return HttpResponseRedirect('/bai-dang/sort=' + TYPE_SORT_BLOG[0] + '&page_id=1/')
    if len(pageNumber) != 0:
        data = getListBlogWithPagination(queryBlog, pageNumber)
        if int(pageNumber) > data.get('totalPages'):
            return HttpResponseRedirect('/bai-dang/sort=' + typeSort + '&page_id=' + str(data.get('totalPages')) + '/')
        return render(request, TEMPLATE_DISPLAY_LIST_BLOG, data)
    return HttpResponseRedirect('/bai-dang/sort=' + typeSort + '&page_id=1/')


def searchBlogWithTitle(request, title, pageNumber):
    if len(pageNumber) == 0:
        return HttpResponseRedirect('/bai-dang/search=' + title + '&page_id=1/')
    queryBlogSearch = Blog.objects.filter(
        title__contains=title, status=DIC_BLOG_STATUS['STATUS_Approve'])
    if queryBlogSearch.exists():
        data = getListBlogWithPagination(queryBlogSearch, pageNumber)
        totalPage = data.get('totalPages')
        if int(pageNumber) > totalPage:
            return HttpResponseRedirect('/bai-dang/search=' + title + '&page_id=' + str(totalPage) + '/')
        return render(request, TEMPLATE_DISPLAY_LIST_BLOG, data)
    else:
        return render(request, TEMPLATE_DISPLAY_LIST_BLOG, {'status': title + ' Not Found'})


def getBlogByURL(request, urlBlog):
    blog = Blog.objects.filter(
        urlBlog=urlBlog, status=DIC_BLOG_STATUS['STATUS_Approve'])
    if blog.exists():
        newView = blog.first().countViewer + 1
        blog.update(countViewer=newView)
        return render(request, TEMPLATE_DISPLAY_SPECIFIC_BLOG, {'data': blog.values, 'status': 'Found'})
    else:
        return render(request, TEMPLATE_DISPLAY_SPECIFIC_BLOG, {'status': 'Not Found'})


def saveBlogIntoDatabase(inputTitle, intputURL, inputDescription, inputContent, inputURLImage):
    newBlog = Blog.objects.create(title=inputTitle,
                                  urlBlog=intputURL,
                                  description=inputDescription,
                                  content=inputContent,
                                  thumbnail=inputURLImage)
    newBlog.save


def checkURLIsUnique(urlNeedCheck):
    return Blog.objects.filter(urlBlog=urlNeedCheck).exists()


def makeNewBlog(formValid):
    title = formValid.cleaned_data['title']

    urlCreate = createURLFromTitleBlog(title)
    while checkURLIsUnique(urlCreate):
        urlCreate = createURLFromTitleBlog(title)
    description = formValid.cleaned_data['description']
    content = formValid.cleaned_data['content']
    urlBlog = urlCreate
    URLImageBlog = getFirstImageInContentBlog(content)
    saveBlogIntoDatabase(title, urlBlog, description, content, URLImageBlog)

def editBlog(request, urlBlogNeedEdit):
    try:
        blogNeedEdit = Blog.objects.get(
            urlBlog=urlBlogNeedEdit, status=DIC_BLOG_STATUS['STATUS_Approve'])
    except Blog.DoesNotExist:
        return HttpResponseRedirect('/bai-dang/')

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blogNeedEdit)
        if form.is_valid():
            form.save()
            return render(request, TEMPLATE_STATUS,
                          {'message': 'Chỉnh sửa thành công!'})
        else:
            return render(request, TEMPLATE_STATUS,
                          {'message': 'Chỉnh sửa thất bại!'})
    elif request.method == 'GET':
        form = BlogForm(instance=blogNeedEdit)
    return render(request, TEMPLATE_DISPLAY_FORM_PUBLISH_BLOG, {'form': form})


def postBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            makeNewBlog(form)
            return render(request, TEMPLATE_STATUS, {'message': 'Đăng bài thành công!'})
        else:
            return render(request, TEMPLATE_STATUS,
                          {'message': 'Đăng bài thất bại!'})
    form = BlogForm()
    return render(request, TEMPLATE_DISPLAY_FORM_PUBLISH_BLOG, {'form': form})
