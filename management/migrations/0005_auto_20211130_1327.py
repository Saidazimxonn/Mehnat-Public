# Generated by Django 3.2.9 on 2021-11-30 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20211130_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livemessage',
            old_name='message_long_uz_Cyrl',
            new_name='message_long_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='livemessage',
            old_name='message_uz_Cyrl',
            new_name='message_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='livemessage',
            old_name='name_uz_Cyrl',
            new_name='name_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='managment',
            old_name='biography_uz_Cyrl',
            new_name='biography_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='managment',
            old_name='functions_tasks_uz_Cyrl',
            new_name='functions_tasks_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='managment',
            old_name='name_uz_Cyrl',
            new_name='name_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='managment',
            old_name='title_uz_Cyrl',
            new_name='title_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Text_uz_Cyrl',
            new_name='Text_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title_uz_Cyrl',
            new_name='title_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='poster',
            old_name='Text_uz_Cyrl',
            new_name='Text_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='poster',
            old_name='title_uz_Cyrl',
            new_name='title_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='regionalcenters',
            old_name='leader_uz_Cyrl',
            new_name='leader_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='regionalcenters',
            old_name='name_uz_Cyrl',
            new_name='name_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='regionalcenters',
            old_name='title_uz_Cyrl',
            new_name='title_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='sections',
            old_name='biography_uz_Cyrl',
            new_name='biography_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='sections',
            old_name='functions_tasks_uz_Cyrl',
            new_name='functions_tasks_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='sections',
            old_name='name_uz_Cyrl',
            new_name='name_oz_Cyrl',
        ),
        migrations.RenameField(
            model_name='sections',
            old_name='title_uz_Cyrl',
            new_name='title_oz_Cyrl',
        ),
    ]