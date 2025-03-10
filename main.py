import reqpip --version


API_KEY = "API"
BASE_URL = "https://api.exchangerate-api.com/v4/latest/"


def convert_currency(amount, from_currency, to_currency):
    url = f"{BASE_URL}{from_currency}"
    response = requests.get(url)
    data = response.json()

    if to_currency in data["rates"]:
        rate = data["rates"][to_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        return None


# Пример использования
amount = float(input("Введите сумму: "))
from_currency = input("Из валюты (например, USD): ").upper()
to_currency = input("В валюту (например, EUR): ").upper()

result = convert_currency(amount, from_currency, to_currency)

if result:
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
else:
    print("Ошибка: некорректная валюта.")
