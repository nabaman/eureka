# Generated by Django 3.1.5 on 2021-02-10 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0006_remove_materi_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='materi',
            name='soal',
            field=models.ManyToManyField(to='learning.Question'),
        ),
    ]