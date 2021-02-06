# Generated by Django 2.1.5 on 2021-02-05 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='post_images')),
                ('body', models.TextField(blank=True, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, default='')),
            ],
        ),
    ]
