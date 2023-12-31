# Generated by Django 4.2.5 on 2023-10-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='background_img',
            field=models.URLField(default='https://fr.newsonthesnow.com/news/wp-content/uploads/sites/3/2021/05/FR-Top-10-des-stations-de-ski-ide%CC%81ales-pour-un-week-end-hero-shutterstock-2-optimized.jpg'),
        ),
        migrations.AddField(
            model_name='event',
            name='logo_img',
            field=models.URLField(default='https://scontent.flyn1-1.fna.fbcdn.net/v/t39.30808-1/309455246_553894126738316_1694927504537490417_n.jpg?stp=dst-jpg_p200x200&_nc_cat=108&ccb=1-7&_nc_sid=754033&_nc_ohc=Ink_21fjHIoAX-i0RB_&_nc_ht=scontent.flyn1-1.fna&oh=00_AfBI6uKyChkwxn8d3qsv-WLQpLOVHJoQ5w9g5oQdW7aA3Q&oe=65245296', max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='nb_max',
            field=models.PositiveSmallIntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='event',
            name='prixA',
            field=models.PositiveSmallIntegerField(default=26),
        ),
        migrations.AlterField(
            model_name='event',
            name='prixNA',
            field=models.PositiveSmallIntegerField(default=35),
        ),
    ]
