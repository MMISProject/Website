# Generated by Django 4.2 on 2023-10-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductId', models.CharField(max_length=122)),
                ('ProductName', models.CharField(max_length=122)),
                ('ProductImage', models.ImageField(upload_to='Images')),
                ('ProductPrice', models.IntegerField()),
            ],
        ),
    ]