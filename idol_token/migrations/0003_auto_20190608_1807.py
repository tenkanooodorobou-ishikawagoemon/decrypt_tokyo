# Generated by Django 2.2.2 on 2019-06-08 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('idol_token', '0002_auto_20190608_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='idol_item',
            name='token',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='idol_item',
            name='idol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='idol_token.Idol'),
        ),
        migrations.AlterField(
            model_name='idol_item',
            name='image',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='image'),
        ),
    ]