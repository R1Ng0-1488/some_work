from django.db import models
from datetime import datetime


class Chart(models.Model):
	function = models.CharField(max_length=20)
	chart = models.ImageField(upload_to='charts/%Y')
	interval = models.IntegerField()
	step = models.IntegerField()
	error = models.CharField(max_length=100, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.function

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
