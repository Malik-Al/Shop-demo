# Generated by Django 2.2 on 2020-09-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200901_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'Новый'), ('payed', 'Оплачен'), ('processing', 'Обработка'), ('delivered', 'Доставлен'), ('canceled', 'Отмена')], default='new', max_length=20, verbose_name='Статус'),
        ),
    ]
