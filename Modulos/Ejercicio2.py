import calendar
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

anyo = 2020
mes = 2
dia = 19

dia_semana = calendar.day_name[calendar.weekday(anyo, mes, dia)]

print("El dia de la semana para el", 1, "de", mes, "del", anyo, "es:",
      dia_semana)