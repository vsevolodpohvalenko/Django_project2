# Generated by Django 3.0.7 on 2020-06-15 18:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200615_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2020, 6, 15, 18, 46, 10, 945319, tzinfo=utc)),
        ),
    ]