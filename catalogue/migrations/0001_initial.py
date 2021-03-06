# Generated by Django 3.0.2 on 2020-02-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datatable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=300)),
                ('brand_name', models.CharField(blank=True, max_length=300)),
                ('product_id', models.IntegerField()),
                ('price', models.FloatField()),
                ('url', models.URLField()),
                ('product_info', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
