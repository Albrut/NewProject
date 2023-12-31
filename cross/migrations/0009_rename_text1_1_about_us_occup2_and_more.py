# Generated by Django 4.1.1 on 2022-12-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross', '0008_remove_more_inform1_title_down_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about_us',
            old_name='text1_1',
            new_name='occup2',
        ),
        migrations.RenameField(
            model_name='about_us',
            old_name='text1_2',
            new_name='occup3',
        ),
        migrations.RemoveField(
            model_name='about_us',
            name='text1_3',
        ),
        migrations.RemoveField(
            model_name='about_us',
            name='text2_1',
        ),
        migrations.RemoveField(
            model_name='about_us',
            name='text2_2',
        ),
        migrations.RemoveField(
            model_name='about_us',
            name='text2_3',
        ),
        migrations.RemoveField(
            model_name='about_us',
            name='text3_1',
        ),
        migrations.RemoveField(
            model_name='about_us',
            name='text3_2',
        ),
        migrations.RemoveField(
            model_name='about_us',
            name='text3_3',
        ),
        migrations.AddField(
            model_name='about_us',
            name='descr1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='about_us',
            name='descr2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='about_us',
            name='descr3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='about_us',
            name='main_thesis',
            field=models.TextField(default='Put on shoes all citizens in Central Asia'),
        ),
        migrations.AddField(
            model_name='about_us',
            name='name1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='about_us',
            name='name2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='about_us',
            name='name3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='about_us',
            name='occup1',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
