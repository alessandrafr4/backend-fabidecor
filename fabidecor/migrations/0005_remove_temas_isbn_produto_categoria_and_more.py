# Generated by Django 4.2.4 on 2023-09-06 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fabidecor', '0004_produto_remove_categoria_isbn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temas',
            name='isbn',
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='categoria', to='fabidecor.categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
