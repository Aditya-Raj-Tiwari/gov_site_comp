# Generated by Django 2.2.1 on 2019-06-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov_site_app', '0014_gaupalikabare'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gaupalikabare',
            old_name='mahila',
            new_name='aakal_mahila',
        ),
        migrations.AddField(
            model_name='gaupalikabare',
            name='jamma',
            field=models.TextField(default=100, max_length=100),
            preserve_default=False,
        ),
    ]
