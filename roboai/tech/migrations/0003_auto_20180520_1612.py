# Generated by Django 2.0.5 on 2018-05-20 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0002_auto_20180520_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='embedded',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='embedded',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='general',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='general',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='imagepro',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='imagepro',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='machine',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='robotics',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='robotics',
            name='updated_at',
        ),
    ]
