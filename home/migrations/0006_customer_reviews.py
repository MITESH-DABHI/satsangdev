# Generated by Django 4.0.5 on 2022-06-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.CharField(blank=True, max_length=600, null=True)),
            ],
        ),
    ]
