def format_price(price):
    price=int(float(price))  #Остался еще вариант с проверкой что передано что-то, что может быть приведено к целому числу, но предположил, что имелась в виду именно такая конструкция ))
    return f'Цена: {price} руб.'

result = format_price('56.24')
print(result)