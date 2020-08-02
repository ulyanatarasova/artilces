import datetime
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    article_title = models.CharField('название статьи', max_length = 200)
    #arcticle_text = models.TextField('текст статьи')
    arcticle_text = RichTextField(blank=True, null=True)
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name='Статья'
        verbose_name_plural= 'Статьи'



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length =200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
#------------------------registration---------------------------



