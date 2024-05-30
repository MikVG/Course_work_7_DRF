# Generated by Django 5.0.4 on 2024-05-30 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_tg_nick'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_chat_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='телеграм chat_id'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tg_nick',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ник в телеграмclear'),
        ),
    ]