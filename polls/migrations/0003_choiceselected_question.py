# Generated by Django 2.1.dev20180318005124 on 2018-03-22 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choiceselected'),
    ]

    operations = [
        migrations.AddField(
            model_name='choiceselected',
            name='question',
            field=models.ForeignKey(default=41, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
            preserve_default=False,
        ),
    ]
