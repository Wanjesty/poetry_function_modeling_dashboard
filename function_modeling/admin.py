from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import data
from function_modeling.views import get_path
from .tasks import create_function_model


@admin.register(data)
class DataAdmin(admin.ModelAdmin):
    def response_add(self, request, obj, post_url_continue=None):
        create_function_model.apply_async((obj.id, ), countdown=5)
        return super().response_add(request, obj, post_url_continue=post_url_continue)
        

    def response_change(self, request, obj):
        create_function_model.apply_async((obj.id, ), countdown=5)
        return super().response_change(request, obj)

    
    list_display = ("function", "get_image", "interval", "step", "date") # Поля отображаемые при просмотре страницы БД
    readonly_fields = ("model", ) # Не редактируемые поля
    search_fields = ("function",) # Поиск по заданным полям   
    fieldsets = (                 # fieldsets настройка полей
        ("Задайте параметры расчета", 
        {"fields" : ("function", "interval", "step")}),
    )


    def get_image(self, obj): #Отображение гарфика, как картинки, а не его ссылки
        if obj.model != get_path(obj.id):
            return obj.model
        return mark_safe(f'<img src={obj.model.url} width="350" height="350"')
        
    get_image.short_description = "График" # Назавание поля для get_image