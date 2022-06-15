from datetime import date, time, datetime, timedelta


data_atual = date.today()
data_atual_str = data_atual.strftime('%A %B %Y')
print(type(data_atual))
print(data_atual_str)
print(type(data_atual_str))

horario = time(hour=15, minute=18,second=30)
print(horario.strftime('%H:%M:%S'))


data_atual = datetime.now()
print(data_atual)
print(data_atual.strftime('%c'))
print(data_atual.weekday())
tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
print(tupla[data_atual.weekday()])

data_criada = datetime(2008, 1 ,20,15,30,20)
print(data_criada)
data_string = '20/04/1991 14:20:55'
data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
print(data_convertida)
nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
print(nova_data)