from typing import Any

import requests
#base_currency ={ 'chf' : 1,
#                 'eur' : 0.94,
#                 'gbr' : 1.1,
#                 'usd' : 0.84,
#                 'uah' : 0.02,
#}


class Price:
    def __init__(self, value: int, currency: str):
        self.value: int = value
        self.currency: str = currency

    def currency_rate(self):
        #self.currency= currency
        url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={self.currency}&to_currency=CHF&apikey=demo'
        r = requests.get(url)
        data = r.json()
        rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        return rate


    def __add__(self, other: Any) -> "Price":
        if not isinstance(other, Price):
            raise ValueError("Can perform operations only with `Price` objects")
        else:
            if self.currency != other.currency:
                total1 = float(self.value * self.currency_rate(self.currency) + other.value * self.currency_rate(other.currency))
                total_in_self_currency = total1 / float(self.currency_rate(self.currency) )
                return Price(total_in_self_currency,self.currency)
            else:
                return Price(self.value + other.value, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            total1 = float(self.value * self.currency_rate(self.currency) - other.value * self.currency_rate(other.currency) )
            total_in_self_currency = total1 / float(self.currency_rate(self.currency) )
            return Price(total_in_self_currency, self.currency)
        else:
            return Price(self.value - other.value , self.currency)





phone = Price(1500, "EUR")
tablet = Price(800, "USD")



phone.currency_rate()

total: Price = phone + tablet
print(f"{total.value} {total.currency}")
dd = phone - tablet
print(dd.value, dd.currency)
