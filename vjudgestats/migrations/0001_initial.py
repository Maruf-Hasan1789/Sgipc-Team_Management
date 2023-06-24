# Generated by Django 4.2.2 on 2023-06-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recentStandings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('rank', models.IntegerField(max_length=10)),
                ('score', models.IntegerField(max_length=10)),
                ('penalty', models.IntegerField(max_length=10)),
            ],
        ),
    ]