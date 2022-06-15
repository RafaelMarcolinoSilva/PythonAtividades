from datetime import date, time


def trabalhando_com_date():
    data_atual = date.today()
    #print(data_atual.strftime('%d/%m/%Y'))# y pequeno traz o ano com 2 dígitos, maiúsculo com 4
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual))
    print(type(data_atual_str))


def trabalhando_com_time():
   horario = time(hour=15, minute=18,second=30 )
   print(horario.strftime('%H:%M: %S'))
    
if __name__ == '__main __':
    trabalhando_com_date()
    trabalhando_com_time()
