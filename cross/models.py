from django.db import models





class Mainpage1_cross(models.Model):
    image1 = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    text1_1 = models.CharField(max_length=50, null=True)
    text1_2 = models.CharField(max_length=50, null=True)
    text1_3 = models.CharField(max_length=50, null=True)
    text2_1 = models.CharField(max_length=50, null=True)
    text2_2 = models.CharField(max_length=50, null=True)
    text2_3 = models.CharField(max_length=50, null=True)
    text3_1 = models.CharField(max_length=50, null=True)
    text3_2 = models.CharField(max_length=50, null=True)
    text3_3 = models.CharField(max_length=50, null=True)

class About_us(models.Model):
    image1 = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    name1 = models.CharField(max_length=50,null=True)
    name2 = models.CharField(max_length=50,null=True)
    name3 = models.CharField(max_length=50,null=True)
    occup1 = models.CharField(max_length=50,null=True)
    occup2 = models.CharField(max_length=50,null=True)
    occup3 = models.CharField(max_length=50,null=True)
    descr1 = models.CharField(max_length=50,null=True)
    descr2 = models.CharField(max_length=50,null=True)
    descr3 = models.CharField(max_length=50,null=True)
    main_thesis = models.TextField(default='Put on shoes all citizens in Central Asia')

class Contact(models.Model):
    name1 = models.CharField(max_length=50, null=True)
    name2 = models.CharField(max_length=50, null=True)
    addres = models.CharField(max_length=50, null=True)
    phone_number1 = models.CharField(max_length=15)
    phone_number2 = models.CharField(max_length=15)
    phone_number3 = models.CharField(max_length=15)
    email1 = models.EmailField(default='albertgadiev@yandex.com')
    email2 = models.EmailField(default='albertgadiev@yandex.com')
    email3 = models.EmailField(default='albertgadiev@yandex.com')
    our_client1 = models.TextField(default='Best of the best')
    our_client2 = models.TextField(default='Better than best')
    image = models.ImageField(default='')




class Products(models.Model):
    image1 = models.ImageField(upload_to='',default='')
    image2 = models.ImageField(upload_to='',default='')
    image3 = models.ImageField(upload_to='',default='')
    name1 = models.CharField(max_length=25,default='')
    name2 = models.CharField(max_length=25,default='')
    name3 = models.CharField(max_length=25,default='')
    name4 = models.CharField(max_length=25,default='')
    name5 = models.CharField(max_length=25,default='')
    name6 = models.CharField(max_length=25, default='')
    image_down1 = models.ImageField(upload_to='')
    image_down2 = models.ImageField(upload_to='')
    image_down3 = models.ImageField(upload_to='')
    cost_1 = models.CharField(max_length=5, default=100)
    cost_2 = models.CharField(max_length=5,default=100)
    cost_3 = models.CharField(max_length=5,default=100)
    cost_4 = models.CharField(max_length=5,default=100)
    cost_5 = models.CharField(max_length=5,default=100)
    cost_6 = models.CharField(max_length=5,default=100)

class More_inform1(models.Model):
    main_title = models.CharField(max_length=30, default='Sneaker')
    main_thesis1 = models.CharField(max_length=100, default='Best solution')
    main_thesis2 = models.CharField(max_length=100, default='Best choice')
    main_title_downer = models.CharField(max_length=30, default='Name Product')
    text_about_product = models.TextField(default='First description about product')
    head_img = models.ImageField(upload_to='',default='')
    quote = models.CharField(max_length=100,default='The best product that I have ever ordered')
    title = models.CharField(max_length=30,default='Unforgettable')
    tittle_descr = models.CharField(max_length=100,default='It does not have analogs')
    main_img = models.ImageField(upload_to='',default='')
    image1 = models.ImageField(upload_to='', default='')
    image2 = models.ImageField(upload_to='', default='')
    image3 = models.ImageField(upload_to='', default='')
    text1_1 = models.TextField(default='')
    text1_2 = models.TextField(default='')
    text1_3 = models.TextField(default='')
    text2_1 = models.TextField(default='')
    text2_2 = models.TextField(default='')
    text2_3 = models.TextField(default='')
    text3_1 = models.TextField(default='')
    text3_2 = models.TextField(default='')
    text3_3 = models.TextField(default='')
class More_inform2(models.Model):
    main_title = models.CharField(max_length=30, default='Sneaker')
    main_thesis1 = models.CharField(max_length=100, default='Best solution')
    main_thesis2 = models.CharField(max_length=100, default='Best choice')
    main_title_downer = models.CharField(max_length=30, default='Name Product')
    text_about_product = models.TextField(default='First description about product')
    head_img = models.ImageField(upload_to='', default='')
    quote = models.CharField(max_length=100, default='The best product that I have ever ordered')
    title = models.CharField(max_length=30, default='Unforgettable')
    tittle_descr = models.CharField(max_length=100, default='It does not have analogs')
    main_img = models.ImageField(upload_to='', default='')
    image1 = models.ImageField(upload_to='', default='')
    image2 = models.ImageField(upload_to='', default='')
    image3 = models.ImageField(upload_to='', default='')
    text1_1 = models.TextField(default='')
    text1_2 = models.TextField(default='')
    text1_3 = models.TextField(default='')
    text2_1 = models.TextField(default='')
    text2_2 = models.TextField(default='')
    text2_3 = models.TextField(default='')
    text3_1 = models.TextField(default='')
    text3_2 = models.TextField(default='')
    text3_3 = models.TextField(default='')
class More_inform3(models.Model):
    main_title = models.CharField(max_length=30, default='Sneaker')
    main_thesis1 = models.CharField(max_length=100, default='Best solution')
    main_thesis2 = models.CharField(max_length=100, default='Best choice')
    main_title_downer = models.CharField(max_length=30, default='Name Product')
    text_about_product = models.TextField(default='First description about product')
    head_img = models.ImageField(upload_to='', default='')
    quote = models.CharField(max_length=100, default='The best product that I have ever ordered')
    title = models.CharField(max_length=30, default='Unforgettable')
    tittle_descr = models.CharField(max_length=100, default='It does not have analogs')
    main_img = models.ImageField(upload_to='', default='')
    image1 = models.ImageField(upload_to='', default='')
    image2 = models.ImageField(upload_to='', default='')
    image3 = models.ImageField(upload_to='', default='')
    text1_1 = models.TextField(default='')
    text1_2 = models.TextField(default='')
    text1_3 = models.TextField(default='')
    text2_1 = models.TextField(default='')
    text2_2 = models.TextField(default='')
    text2_3 = models.TextField(default='')
    text3_1 = models.TextField(default='')
    text3_2 = models.TextField(default='')
    text3_3 = models.TextField(default='')

class More_inform4(models.Model):
    main_title = models.CharField(max_length=30, default='Sneaker')
    main_thesis1 = models.CharField(max_length=100, default='Best solution')
    main_thesis2 = models.CharField(max_length=100, default='Best choice')
    main_title_downer = models.CharField(max_length=30, default='Name Product')
    text_about_product = models.TextField(default='First description about product')
    head_img = models.ImageField(upload_to='', default='')
    quote = models.CharField(max_length=100, default='The best product that I have ever ordered')
    title = models.CharField(max_length=30, default='Unforgettable')
    tittle_descr = models.CharField(max_length=100, default='It does not have analogs')
    main_img = models.ImageField(upload_to='', default='')
    image1 = models.ImageField(upload_to='', default='')
    image2 = models.ImageField(upload_to='', default='')
    image3 = models.ImageField(upload_to='', default='')
    text1_1 = models.TextField(default='')
    text1_2 = models.TextField(default='')
    text1_3 = models.TextField(default='')
    text2_1 = models.TextField(default='')
    text2_2 = models.TextField(default='')
    text2_3 = models.TextField(default='')
    text3_1 = models.TextField(default='')
    text3_2 = models.TextField(default='')
    text3_3 = models.TextField(default='')

class More_inform5(models.Model):
    main_title = models.CharField(max_length=30, default='Sneaker')
    main_thesis1 = models.CharField(max_length=100, default='Best solution')
    main_thesis2 = models.CharField(max_length=100, default='Best choice')
    main_title_downer = models.CharField(max_length=30, default='Name Product')
    text_about_product = models.TextField(default='First description about product')
    head_img = models.ImageField(upload_to='', default='')
    quote = models.CharField(max_length=100, default='The best product that I have ever ordered')
    title = models.CharField(max_length=30, default='Unforgettable')
    tittle_descr = models.CharField(max_length=100, default='It does not have analogs')
    main_img = models.ImageField(upload_to='', default='')
    image1 = models.ImageField(upload_to='', default='')
    image2 = models.ImageField(upload_to='', default='')
    image3 = models.ImageField(upload_to='', default='')
    text1_1 = models.TextField(default='')
    text1_2 = models.TextField(default='')
    text1_3 = models.TextField(default='')
    text2_1 = models.TextField(default='')
    text2_2 = models.TextField(default='')
    text2_3 = models.TextField(default='')
    text3_1 = models.TextField(default='')
    text3_2 = models.TextField(default='')
    text3_3 = models.TextField(default='')

class More_inform6(models.Model):
    main_title = models.CharField(max_length=30, default='Sneaker')
    main_thesis1 = models.CharField(max_length=100, default='Best solution')
    main_thesis2 = models.CharField(max_length=100, default='Best choice')
    main_title_downer = models.CharField(max_length=30, default='Name Product')
    text_about_product = models.TextField(default='First description about product')
    head_img = models.ImageField(upload_to='', default='')
    quote = models.CharField(max_length=100, default='The best product that I have ever ordered')
    title = models.CharField(max_length=30, default='Unforgettable')
    tittle_descr = models.CharField(max_length=100, default='It does not have analogs')
    main_img = models.ImageField(upload_to='', default='')
    image1 = models.ImageField(upload_to='', default='')
    image2 = models.ImageField(upload_to='', default='')
    image3 = models.ImageField(upload_to='', default='')
    text1_1 = models.TextField(default='')
    text1_2 = models.TextField(default='')
    text1_3 = models.TextField(default='')
    text2_1 = models.TextField(default='')
    text2_2 = models.TextField(default='')
    text2_3 = models.TextField(default='')
    text3_1 = models.TextField(default='')
    text3_2 = models.TextField(default='')
    text3_3 = models.TextField(default='')




class Sneakers(models.Model):
    cross_choices = (
        ('Nike', "Nike"),
        ('Vans', "Vans"),
        ('NewBalance', "NewBalance"),
        ('Adidas', "Adidas")
    )
    cross_model = (
        ('Air Jordan 1', "Air Jordan 1"),
        ('Air Jordan 4', "Air Jordan 4"),
        ('Dunk Low Retro Panda', "Dunk Low Retro Panda"),
        ('Air Max 95', "Air Max 95"),
        ('Old Skool', "Old Skool"),
        ('Hi-Top Trainers', "Hi-Top Trainers"),
        ('MADE in USA', "MADE in USA"),
        ('550', "550"),
        ('2002R', "2002R"),
        ('Stan Smith', "Stan Smith"),
        ('Supernova', "Supernova"),
        ('Forum', "Forum"),
        ('Ultraboost', "Ultraboost")
    )

    choice_cross = models.CharField(choices=cross_choices, max_length=100)
    title_cross = models.CharField(choices=cross_model, max_length=100)
    quatity_cross = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    number_phone = models.CharField(max_length=13)
    address = models.CharField(max_length=60)







