# Generated by Django 4.2.4 on 2023-08-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='text',
            new_name='body',
        ),
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(default='default title', max_length=200),
        ),
    ]
