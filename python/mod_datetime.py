from datetime import datetime, timedelta

print(datetime.now())

periodo = timedelta(7)
print(periodo)

print(datetime.now() + periodo)
print(datetime.now().strftime('%d/%m/%Y %H:%M'))

data = 'Jun 1 2005'
print(datetime.strptime(data, '%b %d %Y'))

data1 = datetime.now()
data2 = datetime.now() + periodo

if data1 < data2:
    print("DATA 1 MENOR")

