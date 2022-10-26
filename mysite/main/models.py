from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Project(models.Model):
    name = models.CharField('Pavadinimas', max_length=200, help_text='Įveskite projekto pavadinimą')
    date_start = models.DateField('Pradžios data', blank=True)
    date_end = models.DateField('Pabaigos data', blank=True)
    client = models.ForeignKey('Client', verbose_name='Klientas', on_delete=models.SET_NULL, null=True, blank=True)
    in_charge = models.ForeignKey(User, verbose_name='Projekto Vadovas', on_delete=models.SET_NULL, null=True, blank=True)
    employees = models.ManyToManyField("Employee", verbose_name='Darbuotojai', help_text='Priskirkite darbuotojus šiam projektui')
    tasks = models.ManyToManyField("Task", verbose_name='Užduotys', help_text='Priskirkite darbus šiam projektui')
    bills = models.ManyToManyField("Bill", verbose_name='Sąskaitos', help_text='Priskirkite sąskaitas šiam projektui')
    image = models.ImageField(("Nuotrauka"), upload_to='project_images', null=True, blank=True)
    description = HTMLField(verbose_name='Aprašymas', blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.client}"

    class Meta:
        verbose_name = ('Projektas')
        verbose_name_plural = ('Projektai')


class Client(models.Model):
    first_name = models.CharField('Vardas', max_length=100, help_text='Įveskite kliento vardą')
    last_name = models.CharField('Pavardė', max_length=100, help_text='Įveskite kliento pavardę')
    company = models.CharField('Įmonė', max_length=100, help_text='Įmonės pavadinimas')
    email_field = models.EmailField('Email', max_length=100, help_text='Įveskite kliento elektroninį paštą')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.company})"

    class Meta:
        verbose_name = ('Klientas')
        verbose_name_plural = ('Klientai')


class Employee(models.Model):
    first_name = models.CharField('Vardas', max_length=100, help_text='Įveskite darbuotojo vardą')
    last_name = models.CharField('Pavardė', max_length=100, help_text='Įveskite darbuotojo pavardę')
    position = models.ForeignKey('Position', verbose_name='Pareigos', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"

    class Meta:
        verbose_name = ('Darbuotojas')
        verbose_name_plural = ('Darbuotojai')


class Position(models.Model):
    position_name = models.CharField('Pareigos', max_length=100, help_text='Įveskite darbuotojo pareigas')

    def __str__(self):
        return f"{self.position_name}"

    class Meta:
        verbose_name = ('Pareigos')
        verbose_name_plural = ('Pareigos')


class Task(models.Model):
    task_name = models.CharField('Atliekamas darbas', max_length=100, help_text='Įveskite atliekamą darbą')
    task_comment = models.TextField('Atliekamo darbo pageidavimai', max_length=1000, help_text="Įveskite atliekamo darbo pageidavimus")
    
    TASK_STATUS = (
        ('A', 'Atlikta'),
        ('B', 'Baigta'),
        ('P', 'Pradėta'),
    )

    status = models.CharField('Užduoties statusas', max_length=1, choices = TASK_STATUS, blank=True, default='P', help_text='Užduoties atlikimo statusas')

    def __str__(self):
        return f"{self.task_name} ({self.status})"

    class Meta:
        verbose_name = ('Užduotis')
        verbose_name_plural = ('Užduotys')


class Bill(models.Model):
    issue_date = models.DateField('Sąskaitos išrašymo data', blank=True)
    bill_sum = models.FloatField('Bendra sąskaitos suma', blank=True)

    BILL_STATUS = (
        ('A', 'Apmokėta'),
        ('N', 'Neapmokėta'),
    )

    status = models.CharField('Užduoties statusas', max_length=1, choices = BILL_STATUS, blank=True, default='N', help_text='Užduoties atlikimo statusas')


    def __str__(self):
        return f"{self.bill_sum} ({self.issue_date}) ({self.status})"

    class Meta:
        verbose_name = ('Sąskaita')
        verbose_name_plural = ('Sąskaitos')