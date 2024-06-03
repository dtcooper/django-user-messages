# Generated by Django 5.0.6 on 2024-06-03 08:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('user_messages', '0001_initial'), ('user_messages', '0002_alter_message_index_together'), ('user_messages', '0003_alter_message_index_together_and_more')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at')),
                ('delivered_at', models.DateTimeField(blank=True, null=True, verbose_name='delivered at')),
                ('level', models.IntegerField(verbose_name='level')),
                ('message', models.TextField(verbose_name='message')),
                ('extra_tags', models.TextField(blank=True, verbose_name='extra tags')),
                ('_metadata', models.TextField(blank=True, verbose_name='meta data')),
                ('deliver_once', models.BooleanField(default=True, verbose_name='deliver once')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
                # 'index_together': set(),
                'indexes': [models.Index(models.F('user'), models.F('delivered_at'), name='user_delivered_at')],
            },
        ),
    ]
