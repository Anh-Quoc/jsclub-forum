from django.db import models
from froala_editor.fields import FroalaField

URL_IMAGE_THUMBNAIL_BLOG_DEFAULT = 'uploads/image/blogThumbnailDefault.png'
SET_BLOG_STATUS = {
    ('STATUS_Pending', 'Pending'),
    ('STATUS_Approve', 'Approve')
}


class Blog(models.Model):
    title = models.CharField(max_length=160)  # min = 10
    thumbnail = models.ImageField(
        default=URL_IMAGE_THUMBNAIL_BLOG_DEFAULT)
    urlBlog = models.CharField(unique=True, max_length=200)
    description = models.TextField(max_length=250)
    content = FroalaField(blank=True, null=True)
    countViewer = models.IntegerField(default=0)
    status = models.CharField(
        choices=SET_BLOG_STATUS,
        default='STATUS_Pending',
        max_length=20)
    dateTime = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title
