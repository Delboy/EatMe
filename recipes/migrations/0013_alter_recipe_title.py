# Generated by Django 3.2 on 2022-03-14 12:21

from django.db import migrations, models
import profanity.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_remove_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=100, validators=[profanity.validators.validate_is_profane]),
        ),
    ]
