# Generated by Django 2.0.5 on 2018-05-31 09:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devicelocation', '0004_auto_20180530_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicelocation',
            name='user',
            field=models.ForeignKey(null=True, on_delete='PROTECT', related_name='location_user', to=settings.AUTH_USER_MODEL),
        ),
    ]