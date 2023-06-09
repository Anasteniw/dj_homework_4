# Generated by Django 4.1.7 on 2023-03-19 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название тэга')),
                ('articles', models.ManyToManyField(related_name='tags', to='articles.article')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_tag', models.BooleanField()),
                ('artic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_name', to='articles.article')),
                ('tg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_name', to='articles.tag')),
            ],
        ),
    ]
