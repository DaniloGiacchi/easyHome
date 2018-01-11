from appApi import models
from rest_framework import serializers

class AccomodationsSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = models.Accomodations
        fields = ('title', 'description','price','image','owner','visibility',
                  'guests', 'bedrooms', 'beds','bathroom','services','extraInfo','city',
                  'kindOfHouse','reviews')

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Users
        fields = ('firstName','surname','email','userId')

class ReviewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Reviews
        fields = ('count','stars')

class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Services
        fields = ('wifi','shower','kitchen','surveillanceCamera','HeatingSystem','Television')

class AttractionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Attractions
        fields = ('name','image','city','link')

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ('name','image','city','link')

class DealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Deal
        fields = ('price','accomodations','attractions','restaurant','description')
