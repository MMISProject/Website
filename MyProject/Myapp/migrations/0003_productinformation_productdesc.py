# Generated by Django 4.2.6 on 2023-10-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_userinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinformation',
            name='ProductDesc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]