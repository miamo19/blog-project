# Generated by Django 4.1 on 2022-09-29 04:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_alter_post_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_posts', to='blog.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 29, 4, 51, 19, 857953, tzinfo=datetime.timezone.utc)),
        ),
    ]
