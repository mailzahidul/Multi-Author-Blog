# Generated by Django 3.2.5 on 2021-08-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210730_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Active', 'activae'), ('Deactive', 'deactivae')], default='Active', max_length=10),
        ),
        migrations.AlterField(
            model_name='emailsend',
            name='sender',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
