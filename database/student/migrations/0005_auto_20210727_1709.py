# Generated by Django 3.2.5 on 2021-07-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20210725_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='valid_User_Password',
            field=models.CharField(default=models.CharField(max_length=50, primary_key=True, serialize=False), editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='valid_User_User_Name',
            field=models.CharField(default=models.CharField(max_length=50, primary_key=True, serialize=False), editable=False, max_length=10),
        ),
        migrations.DeleteModel(
            name='Valid_User_Student',
        ),
    ]