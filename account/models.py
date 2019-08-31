from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime


class Bill(models.Model):
    
    CATEGORIES = [('Food', 'Еда'), ('Alcohool', 'Бухло'), 
                    ('Rent', 'Аренда'), ('House', 'Быт'), 
                    ('Hobby', 'Хобби'), ('Education', 'Развитие'),
                    ('Fastfood', 'Фастфуд'), ('Smoking', 'Курево'), ('Transport', 'Транспорт')]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    place = models.CharField(max_length=150)
    summa = models.FloatField()
    created_date = models.DateField(default=datetime.date.today)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='Food')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Position(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    count = models.IntegerField(default=1)
    summa = models.FloatField()
    amount = models.FloatField()
    measure = models.CharField(max_length=1)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
