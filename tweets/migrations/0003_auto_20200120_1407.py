# Generated by Django 3.0.2 on 2020-01-20 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_remove_tweet_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['created_at']},
        ),
    ]
