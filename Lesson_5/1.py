from typing import Any
base_currency ={ 'chf' : 1,
                 'eur' : 0.94,
                 'gbr' : 1.1,
                 'usd' : 0.84,
                 'uah' : 0.02,
}


class Price:
    def __init__(self, value: int, currency: str):
        self.value: int = value
        self.currency: str = currency

    def __add__(self, other: Any) -> "Price":
        if not isinstance(other, Price):
            raise ValueError("Can perform operations only with `Price` objects")
        else:
            if self.currency != other.currency:
                total1 = self.value * base_currency[self.currency] + other.value * base_currency[other.currency]
                total_in_self_currency = total1 / base_currency[self.currency]
                return Price(int(total_in_self_currency),self.currency)
            else:
                return Price(self.value + other.value, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            total1 = self.value * base_currency[self.currency] - other.value * base_currency[other.currency]
            total_in_self_currency = total1 / base_currency[self.currency]
            return Price(int(total_in_self_currency), self.currency)
        else:
            return Price(self.value - other.value , self.currency)





phone = Price(1500, "uah")
tablet = Price(800, "usd")

total: Price = phone + tablet
print(f"{total.value} {total.currency}")
dd = phone - tablet
print(dd.value, dd.currency)
