from django.db import models

class Reviews(models.Model):
    count = models.IntegerField()
    stars = models.IntegerField()

class Users(models.Model):
    firstName = models.CharField(max_length=100, blank=True, default='')
    surname = models.CharField(max_length=100, blank=True, default='')
    email = models.EmailField(max_length=254,default='')
    userId = models.CharField(max_length=100, blank=True, default='',unique = True)
    def __unicode__(self):
        return u"%s" % (self.firstName)
class Services(models.Model):
    wifi = models.BooleanField(default=True)
    shower = models.BooleanField(default=True)
    kitchen = models.BooleanField(default=True)
    surveillanceCamera = models.BooleanField(default=True)
    HeatingSystem = models.BooleanField(default=True)
    Television = models.BooleanField(default=True)

class Accomodations(models.Model):
    
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    price = models.IntegerField()
    image = models.URLField()
    owner = models.ForeignKey(Users,on_delete=models.CASCADE)
    visibility = models.BooleanField(default=True)
    guests = models.IntegerField(default=1)
    bedrooms = models.IntegerField(default=1)
    beds = models.IntegerField(default=1)
    bathroom = models.IntegerField(default=1)
    services = models.ForeignKey(Services,null=False,on_delete=models.CASCADE)
    extraInfo = models.TextField()
    city = models.CharField(max_length=100, blank=False, default='')
    kindOfHouse = models.CharField(max_length=100, blank=True, default='')
    reviews = models.ForeignKey(Reviews,on_delete=models.CASCADE)

class Restaurant(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    image = models.URLField()
    city = models.CharField(max_length=100, blank=False, default='')
    link = models.URLField()


class Attractions(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    image = models.URLField()
    city = models.CharField(max_length=100, blank=False, default='')
    link = models.URLField()

class Deal(models.Model):
    price = models.IntegerField()
    accomodations = models.ForeignKey(Accomodations,on_delete=models.CASCADE)
    attractions = models.ForeignKey(Attractions,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    description = models.TextField(default='')