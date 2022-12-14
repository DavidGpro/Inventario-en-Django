# Generated by Django 4.0.3 on 2022-04-01 15:27

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_alter_tamanosproductos_cantidad_l_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='Alergenos',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('pescado', 'Pescado'), ('fsecos', 'Frutos Secos'), ('lacteos', 'Lácteos'), ('moluscos', 'Moluscos'), ('cgluten', 'Cereales con Gluten'), ('crustaceos', 'Crustáceos'), ('huevos', 'Huevos'), ('cacahuetes', 'Cacahuetes'), ('soja', 'Soja'), ('apio', 'Apio'), ('mostaza', 'Mostaza'), ('sesamo', 'Sésamo'), ('altramuz', 'Altramuces'), ('sulfito', 'Sulfitos')], default=0, max_length=110),
            preserve_default=False,
        ),
    ]
