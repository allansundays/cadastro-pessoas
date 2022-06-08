# Generated by Django 4.0.5 on 2022-06-07 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(blank=True, max_length=256, null=True)),
                ('data_nascimento', models.DateField(null=True)),
                ('ativa', models.BooleanField(default=True)),
            ],
        ),
    ]
