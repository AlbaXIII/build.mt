# Generated by Django 4.2.17 on 2025-01-23 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bgbuild', '0003_bgcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bgreply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_body', models.TextField(max_length=500)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('comment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='bgbuild.bgcomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
