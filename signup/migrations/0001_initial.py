# Generated by Django 3.1.3 on 2023-08-11 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=16, unique=True, verbose_name='유저 이름')),
                ('person_email', models.EmailField(max_length=128, unique=True, verbose_name='유저 이메일')),
                ('person_pw', models.CharField(max_length=128, verbose_name='유저 비밀번호')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'person',
            },
        ),
    ]
