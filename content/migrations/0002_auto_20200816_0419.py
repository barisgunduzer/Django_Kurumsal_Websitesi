# Generated by Django 3.0.8 on 2020-08-16 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
        migrations.DeleteModel(
            name='CImages',
        ),
    ]
