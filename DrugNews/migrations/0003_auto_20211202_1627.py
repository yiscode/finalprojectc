# Generated by Django 3.2.6 on 2021-12-02 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DrugNews', '0002_rename_newtitle_newslist_newstitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newslist',
            old_name='Newsurl',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='newslist',
            old_name='Newstitle',
            new_name='title',
        ),
    ]