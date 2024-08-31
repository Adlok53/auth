# Generated by Django 5.1 on 2024-08-31 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=35)),
                ('salary', models.IntegerField(default=0)),
            ],
        ),
    ]
