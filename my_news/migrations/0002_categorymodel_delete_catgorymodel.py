# Generated by Django 5.0.3 on 2024-03-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CatgoryModel',
        ),
    ]
