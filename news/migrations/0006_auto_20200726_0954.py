# Generated by Django 3.0.8 on 2020-07-26 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200726_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='news_category',
            new_name='category',
        ),
    ]
