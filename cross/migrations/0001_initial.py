# Generated by Django 4.1.1 on 2022-12-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
                ('text1_1', models.CharField(max_length=50, null=True)),
                ('text1_2', models.CharField(max_length=50, null=True)),
                ('text1_3', models.CharField(max_length=50, null=True)),
                ('text2_1', models.CharField(max_length=50, null=True)),
                ('text2_2', models.CharField(max_length=50, null=True)),
                ('text2_3', models.CharField(max_length=50, null=True)),
                ('text3_1', models.CharField(max_length=50, null=True)),
                ('text3_2', models.CharField(max_length=50, null=True)),
                ('text3_3', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=50, null=True)),
                ('name2', models.CharField(max_length=50, null=True)),
                ('name3', models.CharField(max_length=50, null=True)),
                ('insta', models.CharField(max_length=40, null=True)),
                ('phone_number1', models.CharField(max_length=15)),
                ('phone_number2', models.CharField(max_length=15)),
                ('phone_number3', models.CharField(max_length=15)),
                ('adres', models.CharField(max_length=100)),
                ('image_mem', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('image_down1', models.ImageField(upload_to='')),
                ('image_down2', models.ImageField(upload_to='')),
                ('image_down3', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='M_P1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(default='', upload_to='')),
                ('title', models.CharField(default='', max_length=15)),
                ('descr', models.TextField(default='')),
                ('image1', models.ImageField(default='', upload_to='')),
                ('image2', models.ImageField(default='', upload_to='')),
                ('image3', models.ImageField(default='', upload_to='')),
                ('text1_1', models.TextField(default='')),
                ('text1_2', models.TextField(default='')),
                ('text1_3', models.TextField(default='')),
                ('text2_1', models.TextField(default='')),
                ('text2_2', models.TextField(default='')),
                ('text2_3', models.TextField(default='')),
                ('text3_1', models.TextField(default='')),
                ('text3_2', models.TextField(default='')),
                ('text3_3', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='M_P2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(default='', upload_to='')),
                ('title', models.CharField(default='', max_length=15)),
                ('descr', models.TextField(default='')),
                ('image1', models.ImageField(default='', upload_to='')),
                ('image2', models.ImageField(default='', upload_to='')),
                ('image3', models.ImageField(default='', upload_to='')),
                ('text1_1', models.TextField(default='')),
                ('text1_2', models.TextField(default='')),
                ('text1_3', models.TextField(default='')),
                ('text2_1', models.TextField(default='')),
                ('text2_2', models.TextField(default='')),
                ('text2_3', models.TextField(default='')),
                ('text3_1', models.TextField(default='')),
                ('text3_2', models.TextField(default='')),
                ('text3_3', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='M_P3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(default='', upload_to='')),
                ('title', models.CharField(default='', max_length=15)),
                ('descr', models.TextField(default='')),
                ('image1', models.ImageField(default='', upload_to='')),
                ('image2', models.ImageField(default='', upload_to='')),
                ('image3', models.ImageField(default='', upload_to='')),
                ('text1_1', models.TextField(default='')),
                ('text1_2', models.TextField(default='')),
                ('text1_3', models.TextField(default='')),
                ('text2_1', models.TextField(default='')),
                ('text2_2', models.TextField(default='')),
                ('text2_3', models.TextField(default='')),
                ('text3_1', models.TextField(default='')),
                ('text3_2', models.TextField(default='')),
                ('text3_3', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='M_P4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(default='', upload_to='')),
                ('title', models.CharField(default='', max_length=15)),
                ('descr', models.TextField(default='')),
                ('image1', models.ImageField(default='', upload_to='')),
                ('image2', models.ImageField(default='', upload_to='')),
                ('image3', models.ImageField(default='', upload_to='')),
                ('text1_1', models.TextField(default='')),
                ('text1_2', models.TextField(default='')),
                ('text1_3', models.TextField(default='')),
                ('text2_1', models.TextField(default='')),
                ('text2_2', models.TextField(default='')),
                ('text2_3', models.TextField(default='')),
                ('text3_1', models.TextField(default='')),
                ('text3_2', models.TextField(default='')),
                ('text3_3', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='M_P5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(default='', upload_to='')),
                ('title', models.CharField(default='', max_length=15)),
                ('descr', models.TextField(default='')),
                ('image1', models.ImageField(default='', upload_to='')),
                ('image2', models.ImageField(default='', upload_to='')),
                ('image3', models.ImageField(default='', upload_to='')),
                ('text1_1', models.TextField(default='')),
                ('text1_2', models.TextField(default='')),
                ('text1_3', models.TextField(default='')),
                ('text2_1', models.TextField(default='')),
                ('text2_2', models.TextField(default='')),
                ('text2_3', models.TextField(default='')),
                ('text3_1', models.TextField(default='')),
                ('text3_2', models.TextField(default='')),
                ('text3_3', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='M_P6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(default='', upload_to='')),
                ('title', models.CharField(default='', max_length=15)),
                ('descr', models.TextField(default='')),
                ('image1', models.ImageField(default='', upload_to='')),
                ('image2', models.ImageField(default='', upload_to='')),
                ('image3', models.ImageField(default='', upload_to='')),
                ('text1_1', models.TextField(default='')),
                ('text1_2', models.TextField(default='')),
                ('text1_3', models.TextField(default='')),
                ('text2_1', models.TextField(default='')),
                ('text2_2', models.TextField(default='')),
                ('text2_3', models.TextField(default='')),
                ('text3_1', models.TextField(default='')),
                ('text3_2', models.TextField(default='')),
                ('text3_3', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Mainpage1_cross',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
                ('text1_1', models.CharField(max_length=50, null=True)),
                ('text1_2', models.CharField(max_length=50, null=True)),
                ('text1_3', models.CharField(max_length=50, null=True)),
                ('text2_1', models.CharField(max_length=50, null=True)),
                ('text2_2', models.CharField(max_length=50, null=True)),
                ('text2_3', models.CharField(max_length=50, null=True)),
                ('text3_1', models.CharField(max_length=50, null=True)),
                ('text3_2', models.CharField(max_length=50, null=True)),
                ('text3_3', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(default='', upload_to='')),
                ('image2', models.ImageField(default='', upload_to='')),
                ('image3', models.ImageField(default='', upload_to='')),
                ('text1_1', models.TextField()),
                ('text1_2', models.TextField()),
                ('text2_1', models.TextField()),
                ('text2_2', models.TextField()),
                ('image_down1', models.ImageField(upload_to='')),
                ('image_down2', models.ImageField(upload_to='')),
                ('image_down3', models.ImageField(upload_to='')),
                ('cost_1', models.CharField(default=100, max_length=5)),
                ('cost_2', models.CharField(default=100, max_length=5)),
                ('cost_3', models.CharField(default=100, max_length=5)),
                ('cost_4', models.CharField(default=100, max_length=5)),
                ('cost_5', models.CharField(default=100, max_length=5)),
                ('cost_6', models.CharField(default=100, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Sneakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_cross', models.CharField(choices=[('Nike', 'Nike'), ('Vans', 'Vans'), ('NewBalance', 'NewBalance'), ('Adidas', 'Adidas')], max_length=100)),
                ('title_cross', models.CharField(choices=[('Air Jordan 1', 'Air Jordan 1'), ('Air Jordan 4', 'Air Jordan 4'), ('Dunk Low Retro Panda', 'Dunk Low Retro Panda'), ('Air Max 95', 'Air Max 95'), ('Old Skool', 'Old Skool'), ('Hi-Top Trainers', 'Hi-Top Trainers'), ('MADE in USA', 'MADE in USA'), ('550', '550'), ('2002R', '2002R'), ('Stan Smith', 'Stan Smith'), ('Supernova', 'Supernova'), ('Forum', 'Forum'), ('Ultraboost', 'Ultraboost')], max_length=100)),
                ('quatity_cross', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('number_phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=60)),
            ],
        ),
    ]
