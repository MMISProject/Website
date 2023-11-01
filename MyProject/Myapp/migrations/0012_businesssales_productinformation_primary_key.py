# Generated by Django 4.2 on 2023-10-29 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0011_remove_userinformation_businesslogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductId', models.CharField(max_length=122)),
                ('Counter', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='productinformation',
            name='Primary_key',
            field=models.CharField(default=1, max_length=122),
            preserve_default=False,
        ),
    ]
