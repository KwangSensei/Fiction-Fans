# Generated by Django 4.1.2 on 2022-11-08 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiction_fans', '0003_fictionchapter_fictiontitle_delete_story_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fictionchapter',
            old_name='novel_title',
            new_name='fiction_title',
        ),
    ]