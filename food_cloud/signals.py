from django.db.models import signals
from django.dispatch import receiver
from food_cloud.models import Meal, RestaurantProfile

@receiver(signals.pre_save, sender=Meal)
def check_product_description(sender, instance, **kwargs):
    if not instance.description:
        instance.description = 'This is Default Description'

@receiver(signals.post_save, sender=Meal)
def update_restaurant(sender, instance, **kwargs):
		restaurant = RestaurantProfile.objects.get(slug = instance.restaurant_slug)
		restaurant.save()