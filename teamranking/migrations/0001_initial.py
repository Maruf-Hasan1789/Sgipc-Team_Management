# Generated by Django 4.2.2 on 2023-06-19 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teamInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=1500)),
                ('attended_contests', models.IntegerField(default=0)),
            ],
        ),
    ]