# Generated by Django 3.2.4 on 2021-06-14 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formateurs', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stagiaire',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('phone_number', models.CharField(max_length=20)),
                ('specialite', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=False)),
                ('formateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formateurs.formateur')),
            ],
        ),
    ]
