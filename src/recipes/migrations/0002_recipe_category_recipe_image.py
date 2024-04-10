# Generated by Django 4.2.11 on 2024-04-04 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack'), ('dessert', 'Dessert')], default='lunch', max_length=10),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='no_image.jpg', upload_to='recipes'),
        ),
    ]