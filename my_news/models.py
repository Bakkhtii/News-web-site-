from django.db import models


# Create your models here.


class CategoryModel(models.Model):
    category_title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = "news category"
        verbose_name_plural = 'news categories'


class ProductModel(models.Model):
    news_title = models.CharField(max_length=200)
    news_description = models.TextField(null=True)
    news_categories = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    news_image = models.FileField(upload_to="news_images")
    news_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = "new"
        verbose_name_plural = 'news'
