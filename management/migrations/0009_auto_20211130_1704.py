# Generated by Django 3.2.9 on 2021-11-30 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_auto_20211130_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livemessage',
            name='message_ko',
        ),
        migrations.RemoveField(
            model_name='livemessage',
            name='message_long_ko',
        ),
        migrations.RemoveField(
            model_name='livemessage',
            name='message_long_oz',
        ),
        migrations.RemoveField(
            model_name='livemessage',
            name='message_oz',
        ),
        migrations.RemoveField(
            model_name='livemessage',
            name='name_ko',
        ),
        migrations.RemoveField(
            model_name='livemessage',
            name='name_oz',
        ),
        migrations.RemoveField(
            model_name='managment',
            name='biography_ko',
        ),
        migrations.RemoveField(
            model_name='managment',
            name='biography_oz',
        ),
        migrations.RemoveField(
            model_name='managment',
            name='functions_tasks_ko',
        ),
        migrations.RemoveField(
            model_name='managment',
            name='functions_tasks_oz',
        ),
        migrations.RemoveField(
            model_name='managment',
            name='name_ko',
        ),
        migrations.RemoveField(
            model_name='managment',
            name='name_oz',
        ),
        migrations.RemoveField(
            model_name='managment',
            name='title_ko',
        ),
        migrations.RemoveField(
            model_name='managment',
            name='title_oz',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Text_ko',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Text_oz',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_ko',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_oz',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='Text_ko',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='Text_oz',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='title_ko',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='title_oz',
        ),
        migrations.RemoveField(
            model_name='regionalcenters',
            name='leader_ko',
        ),
        migrations.RemoveField(
            model_name='regionalcenters',
            name='leader_oz',
        ),
        migrations.RemoveField(
            model_name='regionalcenters',
            name='name_ko',
        ),
        migrations.RemoveField(
            model_name='regionalcenters',
            name='name_oz',
        ),
        migrations.RemoveField(
            model_name='regionalcenters',
            name='title_ko',
        ),
        migrations.RemoveField(
            model_name='regionalcenters',
            name='title_oz',
        ),
        migrations.RemoveField(
            model_name='sections',
            name='biography_ko',
        ),
        migrations.RemoveField(
            model_name='sections',
            name='biography_oz',
        ),
        migrations.RemoveField(
            model_name='sections',
            name='functions_tasks_ko',
        ),
        migrations.RemoveField(
            model_name='sections',
            name='functions_tasks_oz',
        ),
        migrations.RemoveField(
            model_name='sections',
            name='name_ko',
        ),
        migrations.RemoveField(
            model_name='sections',
            name='name_oz',
        ),
        migrations.RemoveField(
            model_name='sections',
            name='title_ko',
        ),
        migrations.RemoveField(
            model_name='sections',
            name='title_oz',
        ),
    ]
