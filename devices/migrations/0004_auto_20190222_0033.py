# Generated by Django 2.1.4 on 2019-02-22 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_auto_20190221_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='status',
            field=models.CharField(choices=[('H', 'Habilitado'), ('I', 'Inabilitado')], default='I', max_length=15, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='position',
            name='c',
            field=models.IntegerField(default=2, verbose_name='C'),
            preserve_default=False,
        ),
    ]
