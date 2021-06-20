from work.celery import app
import numpy as np 
import io
import matplotlib.pyplot as plt
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from django.core.files import File


from celery import shared_task
from .models import Chart

def execute(func):
    d = {'e': np.e, 'log': np.log, 'cos': np.cos,
         'sin': np.sin, 'tan': np.tan, 'arcsin': np.arcsin,
         'arccos': np.arccos, 'arctan': np.arctan}
    return lambda t: eval(func, {**d, 't': t})

@app.task
def make_a_chart(id):
    flag = True
    while flag:
        try: 
            obj = Chart.objects.get(id=id)
            flag = False
        except Chart.DoesNotExist:
            pass

    y2 = execute(obj.function)
    flg = plt.subplots()

    end = timezone.now().timestamp()
    start = end - obj.interval * 24 * 3600
    step = obj.step * 3600
    x2 = np.arange(int(start), int(end), int(step))

    figure = io.BytesIO()
    name = f'{obj.id}-chart.jpg'

    try:
        plt.plot(x2, y2(x2))
    except Exception as e:
        obj.error = e.args[0]
        obj.save()
        return

    plt.savefig(figure, format='jpg')
    obj.chart.save(name, figure, save=True)

