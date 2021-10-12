from function_modeling_dashboard.celery import app
from .views import save, create_time_period_with_step, get_path
import matplotlib.pyplot as plt
from .models import data


@app.task
def create_function_model(id_number, *args): # Создание графика
    data_line = data.objects.filter(id=id_number)
    time_period_with_step = create_time_period_with_step(data_line[0].interval, data_line[0].step)
    if time_period_with_step == "date value out of range":
        write_to_model = "date value out of range"
    else:
        try:
            y_values = [eval(data_line[0].function) for t in [t.hour for t in time_period_with_step]]
        except ZeroDivisionError as er:
            write_to_model = str(er)
        except NameError as er:
            write_to_model = str(er)
        except SyntaxError as er:
            write_to_model = str(er)
        except TypeError as er:
            write_to_model = str(er)
        else:
            plt.grid(True)
            plt.plot(time_period_with_step, y_values, color = 'blue')
            plt.scatter(time_period_with_step, y_values, color = 'red')
            plt.gcf().autofmt_xdate()
            save(str(data_line[0].id))
            plt.close()
            write_to_model = get_path(data_line[0].id)
    data_line = data.objects.get(id=id_number)
    data_line.model = write_to_model
    data_line.save(update_fields=['model'])