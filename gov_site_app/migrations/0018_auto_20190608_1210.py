# Generated by Django 2.2.1 on 2019-06-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov_site_app', '0017_auto_20190608_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='suchanaitems',
            name='Suchana3_heading',
            field=models.CharField(default='Title', max_length=32),
        ),
        migrations.AddField(
            model_name='suchanaitems',
            name='Suchana3_suchana_photo',
            field=models.ImageField(blank=True, null=True, upload_to='suchana'),
        ),
        migrations.AddField(
            model_name='suchanaitems',
            name='Suchana3_suchana_photo_description',
            field=models.TextField(default='Title', max_length=200),
        ),
        migrations.AddField(
            model_name='suchanaitems',
            name='Suchana3_suchana_photo_name',
            field=models.CharField(default='Title', max_length=32),
        ),
    ]