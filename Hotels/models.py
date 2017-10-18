from django.db import models
import random


class Region(models.Model):
    title = models.CharField(
        'title', 
    	max_length = 64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'регион'
        verbose_name_plural = 'регионы'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Hotel(models.Model):
    title = models.CharField(
        'title', 
    	max_length = 64)
    region = models.ForeignKey(
        Region, 
    	verbose_name='Region', related_query_name="hotels")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'отель'
        verbose_name_plural = 'отели'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



def inquiries(request):

# кол-во отелей всего
    count_h = Hotel.objects.count() 

# все отели определённого региона
    spec_h = Hotel.objects.filter(region__title="") 

# Вывести 5 случайных отелей какого-то региона. Способ 1
   	rnd = Hotel.objects.filter(region__title="").order_by('?')[:5]

# Вывести 5 случайных отелей какого-то региона. Способ 2
    ListSet = list(Hotel.objects.filter(region__title="")
    random.shuffle(ListSet)
    ListSet[:5]

# Получить все отели, отсортированные по названию региона
	sort_h = Hotel.objects.order_by('region__title')

# Получить все отели, отсортированные по названию отеля
	sort_r = Hotel.objects.order_by('title')

# Получить все отели у которых выбран регион
	notNULL_h = Hotel.objects.filter(region__isnull=False)

# Получить все регионы, у которых больше 5 отелей
    q = Region.objects.annotate(Count('hotels'))
    a = len(Region.objects.all())
    for x in range(a):
        if q[x].hotels__count > 5:
            Region.objects.filter(id = x+1)

# Получить первый отель, название которого начинается с "Гранд"
	grand_h = Hotel.objects.filter(title__startswith="Гранд")[0]