# Generated by Django 3.2.16 on 2022-11-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_choice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multi_choice',
            name='date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='multi_choice',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]