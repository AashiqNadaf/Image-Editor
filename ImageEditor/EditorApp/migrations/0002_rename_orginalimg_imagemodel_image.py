# Generated by Django 3.2.5 on 2022-08-28 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EditorApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagemodel',
            old_name='orginalImg',
            new_name='image',
        ),
    ]
