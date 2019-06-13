# Generated by Django 2.2.1 on 2019-06-08 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov_site_app', '0018_auto_20190608_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suchanaitems',
            name='Suchana1_suchana_photo_description',
            field=models.TextField(blank=True, default='Title', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='suchanaitems',
            name='Suchana1_suchana_photo_name',
            field=models.CharField(blank=True, default='Title', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='suchanaitems',
            name='Suchana2_suchana_photo_description',
            field=models.TextField(blank=True, default='Title', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='suchanaitems',
            name='Suchana2_suchana_photo_name',
            field=models.CharField(blank=True, default='Title', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='suchanaitems',
            name='Suchana3_heading',
            field=models.CharField(blank=True, default='Title', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='suchanaitems',
            name='Suchana3_suchana_photo_description',
            field=models.TextField(blank=True, default='Title', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='suchanaitems',
            name='Suchana3_suchana_photo_name',
            field=models.CharField(blank=True, default='Title', max_length=32, null=True),
        ),
    ]