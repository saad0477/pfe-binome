# Generated by Django 3.2.4 on 2021-06-16 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formateurs', '0001_initial'),
        ('stagiaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stagiaire',
            name='formateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='formateurs.formateur'),
        ),
    ]
