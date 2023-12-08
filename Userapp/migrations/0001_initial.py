# Generated by Django 4.2.7 on 2023-12-08 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('user_password', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='UserMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField(default=8600)),
                ('expired_date', models.DateField()),
                ('money', models.IntegerField()),
                ('card_holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='AllMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_money', models.IntegerField(default=0)),
                ('type_of_money', models.CharField(choices=[('Kirim', 'Kirim'), ('Chiqim', 'Chiqim')], max_length=6)),
                ('date', models.DateField(auto_now_add=True)),
                ('category_money', models.CharField(choices=[('Oziq-ovqat', 'Oziq-ovqat'), ('Transport', 'Transport'), ('Kiyim-kechak', 'Kiyim-kechak'), ('Komunal', 'Komunal'), ('Axborot-vositalari', 'Axborot-vositalari'), ('Kafe-restoran', 'Kafe-restoran'), ('Taksi', 'Taksi'), ('Xizmatlar', 'Xizmatlar')], max_length=30)),
                ('comment', models.TextField(blank=True)),
                ('user_n', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Userapp.user')),
            ],
        ),
    ]
