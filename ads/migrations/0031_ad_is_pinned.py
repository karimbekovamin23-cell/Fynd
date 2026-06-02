from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0030_create_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='is_pinned',
            field=models.BooleanField(default=False, verbose_name='Закреплено'),
        ),
    ]
