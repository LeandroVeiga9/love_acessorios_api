# Generated by Django 4.2.7 on 2024-01-01 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_variant_image_variant_thumbnail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('FINISHED', 'finished')], default='ACTIVE', max_length=10),
        ),
    ]
