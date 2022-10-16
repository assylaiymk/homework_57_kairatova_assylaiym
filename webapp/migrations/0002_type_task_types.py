# Generated by Django 4.1.2 on 2022-10-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='types',
            field=models.ManyToManyField(blank=True, related_name='types', to='webapp.type', verbose_name='Type'),
        ),
    ]
