from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    category_title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)


    def str(self):
        return self.category_title

    class Meta:
        verbose_name = "news category"
        verbose_name_plural = 'news categories'


class ProductModel(models.Model):
    news_title = models.CharField(max_length=30)
    news_description = models.TextField
    news_image = models.FileField(upload_to="news_images")
    news_created_at = models.DateTimeField(auto_now_add=True)


    def str(self):
        return self.product_title

    class Meta:
        verbose_name = "new"
        verbose_name_plural = 'news'