# Generated by Django 3.2.8 on 2021-11-09 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
