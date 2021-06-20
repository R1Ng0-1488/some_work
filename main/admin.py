from django.contrib import admin
from django.utils.html import mark_safe

from .models import Chart


@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
	list_display = ('id', 'function', 'get_image', 'interval', 'step', 'date')
	fields = ('function', 'interval', 'step',)

	def get_image(self, obj):
		if obj.error:
			return mark_safe(obj.error)
		elif obj.chart:
			return mark_safe(f'<img src="{obj.chart.url}" widgth="200" height="200">')
		else:
			return ''
	get_image.short_description = 'График'