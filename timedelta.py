from datetime import datetime

def info(then):
    diff = then-datetime.now()
    hours = diff.seconds // 3600
    minutes =  (diff.seconds % 3600) // 60 
    seconds = (diff.seconds % 3600) % 60
    print('Осталось:\nДней: %s\n' % diff.days +
         'Часов: %s\nМинут: %s\nСекунд: %s' % (hours, minutes, seconds))

info(datetime(2019, 9, 2, 8, 30))    
