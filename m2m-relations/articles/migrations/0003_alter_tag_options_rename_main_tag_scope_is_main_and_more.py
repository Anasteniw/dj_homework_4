# Generated by Django 4.1.7 on 2023-03-19 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_options_tag_scope'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.RenameField(
            model_name='scope',
            old_name='main_tag',
            new_name='is_main',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='articles',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', through='articles.Scope', to='articles.tag'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='artic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='tg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag'),
        ),
    ]