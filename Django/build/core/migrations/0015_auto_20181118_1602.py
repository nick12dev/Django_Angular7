# Generated by Django 2.1.2 on 2018-11-18 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20181113_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapSubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='map_subcategories', to='core.SubCategory')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('belts', 'belts'), ('scarves', 'scarves'), ('bras', 'bras'), ('sweatpants', 'sweatpants'), ('sneakers', 'sneakers'), ('coats', 'coats'), ('turtlenecks', 'turtlenecks'), ('vests', 'vests'), ('socks', 'socks'), ('corsets-and-bodysuits', 'corsets-and-bodysuits'), ('thongs', 'thongs'), ('bombers', 'bombers'), ('wallets', 'wallets'), ('jeans', 'jeans'), ('boxers', 'boxers'), ('backpacks', 'backpacks'), ('Hoodies-and-Zipups', 'Hoodies-and-Zipups'), ('hats', 'hats'), ('dress-pants', 'dress-pants'), ('sweatshirts', 'sweatshirts'), ('dress-shirt', 'dress-shirt'), ('t-shirt', 't-shirt'), ('tank-tops', 'tank-tops'), ('pants', 'pants'), ('suits', 'suits'), ('shorts', 'shorts'), ('other', 'other'), ('crewnecks', 'crewnecks'), ('polo', 'polo'), ('jewelry', 'jewelry'), ('joggers', 'joggers'), ('gloves', 'gloves'), ('eyewear', 'eyewear'), ('trousers', 'trousers'), ('long-sleeves', 'long-sleeves'), ('briefs', 'briefs'), ('blazers', 'blazers'), ('cardigans', 'cardigans'), ('loafers', 'loafers'), ('jackets', 'jackets'), ('formal-wear', 'formal-wear')], max_length=300, null=True),
        ),
    ]
