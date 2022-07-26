from .models import SET_BLOG_STATUS, URL_IMAGE_THUMBNAIL_BLOG_DEFAULT

TEMPLATE_DISPLAY_LIST_BLOG = 'pages/blog.html'
TEMPLATE_DISPLAY_SPECIFIC_BLOG = 'pages/post.html'
TEMPLATE_DISPLAY_FORM_PUBLISH_BLOG = 'pages/postform.html'
NUMBER_BLOG_IN_ONE_PAGE = 5
TYPE_SORT_BLOG = ['date', 'views']
URL_GET_LIST_BLOG_DEFAULT = '/bai-dang/sort=date&page_id=1/'
LENGTH_STRING_RANDOM_FOR_URL = 10
TEMPLATE_STATUS = 'pages/status.html'

DIC_BLOG_STATUS = {}
for status in SET_BLOG_STATUS:
    DIC_BLOG_STATUS[status[0]] = status[0]
