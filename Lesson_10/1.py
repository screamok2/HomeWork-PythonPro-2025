from typing import Any

import requests


class Price:
    def __init__(self, value: int, currency: str):
        self.value: int = value
        self.currency: str = currency

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
                return Price(total_in_self_currency,self.currency)
            else:
                return Price(self.value + other.value, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            total1 = float(self.value * self.currency_rate(self.currency) - other.value * self.currency_rate(other.currency) )
            return Price(total_in_self_currency, self.currency)
        else:
            return Price(self.value - other.value , self.currency)





phone = Price(1500, "EUR")




total: Price = phone + tablet
