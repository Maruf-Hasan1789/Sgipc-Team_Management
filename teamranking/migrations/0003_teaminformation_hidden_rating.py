# Generated by Django 4.2.2 on 2023-06-23 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamranking', '0002_teaminformation_rating_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaminformation',
            name='hidden_rating',
            field=models.IntegerField(default=1500),
        ),
    ]