# Generated by Django 3.2.9 on 2021-11-30 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0003_auto_20211110_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='livemessage',
            name='message_long_uz_Cyrl',
            field=models.TextField(null=True, verbose_name='Message long'),
        ),
        migrations.AddField(
            model_name='livemessage',
            name='message_uz_Cyrl',
            field=models.CharField(max_length=100, null=True, verbose_name='Message'),
        ),
        migrations.AddField(
            model_name='livemessage',
            name='name_uz_Cyrl',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='managment',
            name='biography_uz_Cyrl',
            field=models.TextField(blank=True, null=True, verbose_name='Tarjimai hol'),
        ),
        migrations.AddField(
            model_name='managment',
            name='functions_tasks_uz_Cyrl',
            field=models.TextField(blank=True, null=True, verbose_name='Funksiya va vazifalar'),
        ),
        migrations.AddField(
            model_name='managment',
            name='name_uz_Cyrl',
            field=models.CharField(max_length=250, null=True, verbose_name='F.I.SH'),
        ),
        migrations.AddField(
            model_name='managment',
            name='title_uz_Cyrl',
            field=models.CharField(max_length=250, null=True, verbose_name='Lavozimi'),
        ),
        migrations.AddField(
            model_name='post',
            name='Text_uz_Cyrl',
            field=models.TextField(blank=True, null=True, verbose_name='Matin'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_uz_Cyrl',
            field=models.CharField(max_length=300, null=True, verbose_name='Qisqa matn'),
        ),
        migrations.AddField(
            model_name='regionalcenters',
            name='leader_uz_Cyrl',
            field=models.CharField(max_length=250, null=True, verbose_name="F.I.SH BOshqarma boshlig'i"),
        ),
        migrations.AddField(
            model_name='regionalcenters',
            name='name_uz_Cyrl',
            field=models.CharField(max_length=250, null=True, verbose_name='Hududiy boshqarma nomi'),
        ),
        migrations.AddField(
            model_name='regionalcenters',
            name='title_uz_Cyrl',
            field=models.CharField(max_length=250, null=True, verbose_name='Manzili'),
        ),
        migrations.AddField(
            model_name='sections',
            name='biography_uz_Cyrl',
            field=models.TextField(blank=True, null=True, verbose_name='Tarjimai hol'),
        ),
        migrations.AddField(
            model_name='sections',
            name='functions_tasks_uz_Cyrl',
            field=models.TextField(blank=True, null=True, verbose_name='Funksiya va vazifalar'),
        ),
        migrations.AddField(
            model_name='sections',
            name='name_uz_Cyrl',
            field=models.CharField(max_length=250, null=True, verbose_name='F.I.SH'),
        ),
        migrations.AddField(
            model_name='sections',
            name='title_uz_Cyrl',
            field=models.CharField(max_length=250, null=True, verbose_name='Lavozimi'),
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Qisqa matn')),
                ('title_uz', models.CharField(max_length=300, null=True, verbose_name='Qisqa matn')),
                ('title_uz_Cyrl', models.CharField(max_length=300, null=True, verbose_name='Qisqa matn')),
                ('title_ko', models.CharField(max_length=300, null=True, verbose_name='Qisqa matn')),
                ('title_ru', models.CharField(max_length=300, null=True, verbose_name='Qisqa matn')),
                ('title_en', models.CharField(max_length=300, null=True, verbose_name='Qisqa matn')),
                ('Text', models.TextField(blank=True, null=True, verbose_name='Matin')),
                ('Text_uz', models.TextField(blank=True, null=True, verbose_name='Matin')),
                ('Text_uz_Cyrl', models.TextField(blank=True, null=True, verbose_name='Matin')),
                ('Text_ko', models.TextField(blank=True, null=True, verbose_name='Matin')),
                ('Text_ru', models.TextField(blank=True, null=True, verbose_name='Matin')),
                ('Text_en', models.TextField(blank=True, null=True, verbose_name='Matin')),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Muallif')),
            ],
            options={
                'verbose_name': "E'lon",
                'verbose_name_plural': "E'lonlar",
            },
        ),
    ]