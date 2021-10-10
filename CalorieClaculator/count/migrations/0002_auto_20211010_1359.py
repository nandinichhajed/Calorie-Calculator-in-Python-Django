# Generated by Django 3.2.8 on 2021-10-10 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='calories',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='carbohydrates',
        ),
        migrations.AddField(
            model_name='fooditem',
            name='calorie',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='carbohydrate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner'), ('snacks', 'snacks')], max_length=50),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='fats',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='protein',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='userfooditem',
            name='fooditem',
            field=models.ManyToManyField(to='count.Fooditem'),
        ),
    ]