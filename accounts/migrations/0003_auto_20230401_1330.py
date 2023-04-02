# Generated by Django 3.2.6 on 2023-04-01 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230401_0322'),
    ]

    operations = [
        migrations.DeleteModel(
            name='others',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='investment_balance',
            new_name='main_balance',
        ),
        migrations.RemoveField(
            model_name='user',
            name='has_active_investment',
        ),
        migrations.RemoveField(
            model_name='user',
            name='investment_start_date',
        ),
    ]
