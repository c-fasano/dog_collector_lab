# Generated by Django 3.2.9 on 2021-11-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_walk'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='walk',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='walk',
            name='date',
            field=models.DateField(verbose_name='Walk Date'),
        ),
    ]
