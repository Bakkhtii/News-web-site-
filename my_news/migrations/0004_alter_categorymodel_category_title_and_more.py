# Generated by Django 5.0.3 on 2024-03-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_news', '0003_productmodel_alter_categorymodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='category_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='news_title',
            field=models.CharField(max_length=200),
        ),
    ]
