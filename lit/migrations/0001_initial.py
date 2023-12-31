# Generated by Django 4.2.4 on 2023-08-28 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
                ('search_date', models.DateTimeField(auto_now_add=True)),
                ('num_results', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
