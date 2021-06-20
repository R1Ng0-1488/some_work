from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Chart
from .tasks import make_a_chart

@receiver(post_save, sender=Chart)
def my_handler(sender, **kwargs):
	if kwargs['instance'].error:
		return
	if not kwargs['instance'].chart: 
		make_a_chart.delay(kwargs['instance'].id)