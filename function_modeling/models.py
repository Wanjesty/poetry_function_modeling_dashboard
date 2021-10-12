from django.db import models

class data(models.Model):
    """Данные построения графика"""
    function = models.CharField("Функция, t", max_length=255)
    model = models.ImageField("График", upload_to="graphs/")
    interval = models.IntegerField("Интервал, dt(день)")
    step = models.IntegerField("Шаг, dt(час)")
    date = models.DateTimeField("Время", auto_now_add=True)

    def __str__(self):
        return self.function

