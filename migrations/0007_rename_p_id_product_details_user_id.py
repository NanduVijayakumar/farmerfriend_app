# Generated by Django 3.2 on 2021-05-06 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_product_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_details',
            old_name='p_id',
            new_name='user_id',
        ),
    ]