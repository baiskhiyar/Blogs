# Generated by Django 4.1.7 on 2023-03-11 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0005_rename_name_history_searched_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogtagmapping',
            old_name='tag_ids',
            new_name='tag_id',
        ),
    ]
