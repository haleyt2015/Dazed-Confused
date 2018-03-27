# Generated by Django 2.0.1 on 2018-03-27 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_type', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['prod_type'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='products',
            unique_together={('prod_type',)},
        ),
    ]
