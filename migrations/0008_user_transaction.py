# Generated by Django 3.2 on 2021-06-02 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_p_id_product_details_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('amt', models.FloatField()),
                ('card_no', models.CharField(max_length=25)),
                ('cvv', models.CharField(max_length=25)),
                ('expiry', models.CharField(max_length=25)),
                ('dt', models.CharField(max_length=25)),
                ('tm', models.CharField(max_length=25)),
            ],
        ),
    ]
