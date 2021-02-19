# Generated by Django 3.1.5 on 2021-02-19 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ImageMateri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Question_Kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_kategori_name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.question_kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('1', 'MUDAH'), ('2', 'SEDANG'), ('3', 'SULIT')], max_length=2, null=True)),
                ('question', models.CharField(max_length=200, null=True)),
                ('q_type', models.CharField(choices=[('text', 'text'), ('choice', 'choice')], max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='learning.choice')),
                ('choices', models.ManyToManyField(to='learning.Choice')),
                ('img', models.ManyToManyField(to='learning.ImageMateri')),
                ('q_kategori', models.ForeignKey(limit_choices_to={'parent': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='learning.question_kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Materi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('materi', models.TextField(null=True)),
                ('gambar', models.ManyToManyField(to='learning.ImageMateri')),
                ('soal', models.ManyToManyField(to='learning.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.data_teacher')),
            ],
        ),
    ]
