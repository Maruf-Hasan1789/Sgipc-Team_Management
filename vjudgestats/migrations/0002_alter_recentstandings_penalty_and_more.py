# Generated by Django 4.2.2 on 2023-06-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vjudgestats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentstandings',
            name='penalty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recentstandings',
            name='rank',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recentstandings',
            name='score',
            field=models.IntegerField(),
        ),
    ]
