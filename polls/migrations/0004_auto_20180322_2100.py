# Generated by Django 2.1.dev20180318005124 on 2018-03-22 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choiceselected_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choiceselected',
            old_name='user_id',
            new_name='user',
        ),
    ]
