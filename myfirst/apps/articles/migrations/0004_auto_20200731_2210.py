# Generated by Django 3.0.8 on 2020-07-31 19:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_user_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_data',
        ),
        migrations.AlterField(
            model_name='article',
            name='arcticle_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
