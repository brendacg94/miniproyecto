# Generated by Django 3.2.12 on 2022-02-07 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bank', '0001_initial'),
        ('users', '0002_delete_bank_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account_number', models.CharField(max_length=255, verbose_name='Número de cuenta')),
                ('id_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank.bank', verbose_name='Banco')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Cuenta de Banco',
                'verbose_name_plural': 'Cuentas de Banco',
            },
        ),
    ]
