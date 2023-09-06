from django.db import models

# Create your models here.

class Services(models.Model):
    title= models.CharField(max_length=100, verbose_name='Title', help_text='The title i occupy')
    icon = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Services"

class Technology(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', help_text='The technology i use')
    icon = models.ImageField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Technology"

class Points(models.Model):
    points =models.CharField(max_length=1000)

    
    def __str__(self):
        return self.points

class Experience(models.Model):
    title= models.CharField(max_length=100, verbose_name='Title', help_text='My experience')
    icon = models.ImageField()
    iconBg = models.CharField(max_length=100, verbose_name='icon color', help_text='icon color')
    company_name = models.CharField(max_length=100, verbose_name='Company', help_text='Company experience')
    date = models.CharField(max_length=100, verbose_name='Date', help_text=' experience date')
    points = models.ManyToManyField(Points)

    
    def __str__(self):
        return self.title

class Tags(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', help_text='The technology i use')
    color = models.CharField(max_length=100, verbose_name='Color', help_text='The color i choose')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Tags"


class Projects(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', help_text='The name of the project')
    description = models.TextField( verbose_name='Description', help_text='The description')
    tags = models.ManyToManyField(Tags)
    image = models.ImageField()
    source_code_link = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Projects"

class Testimonials(models.Model):
    testimonial = models.TextField(help_text="The testimonial")
    name = models.CharField(max_length=200, help_text="Name of the individual")
    designation = models.CharField(max_length=200, help_text="office of the individual")
    company = models.CharField(max_length=200, help_text="company of the individual")
    image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural='Testimonials'

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=1000, verbose_name='Name of Sender:', help_text='Name of the sender sending an email')
    #email = models.EmailField(verbose_name='Email of Sender:', help_text='Contact email of the sender')
    message = models.TextField(verbose_name='Content Message:', help_text='Message received')

    class Meta:
        verbose_name='My Contact Message'
        verbose_name_plural='My Contact Messages'

    def __str__(self):
        return self.name



    


