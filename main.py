import requests
import customtkinter

customtkinter.set_appearance_mode("system")

app = customtkinter.CTk()
app.geometry("320x350")
app.minsize(320, 350)
app.title("Currency Converter")

BASE_URL = "https://api.exchangerate-api.com/v4/latest/"

CURRENCIES = [
    "USD", "EUR", "UAH", "GBP", "JPY", "CNY", "CHF", "CAD", "AUD", "NZD",
    "SEK", "NOK", "DKK", "PLN", "HUF", "CZK", "SGD", "HKD", "KRW", "INR",
    "BRL", "MXN", "ZAR", "TRY", "RUB", "THB", "IDR", "MYR", "PHP"
]


def convert_currency(amount, from_currency, to_currency):
    try:
        url = f"{BASE_URL}{from_currency}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Проверка на ошибки

        data = response.json()
        rates = data.get("rates", {})

        if to_currency not in rates:
            return f"Error: Currency {to_currency} not found"

        converted = rates[to_currency] * amount
        return round(converted, 2)

    except requests.exceptions.RequestException:
        return "Error: No connection to API"


def button_callback():
    try:
        amount = float(entry.get())
        from_currency = optionmenu_var2.get()
        to_currency = optionmenu_var.get()

        if from_currency == to_currency:
            result_label.configure(text="Choose different currencies!")
            return

        result = convert_currency(amount, from_currency, to_currency)
        result_label.configure(text=f"Converted: {amount} {from_currency} = {result} {to_currency}")
    except ValueError:
        result_label.configure(text="Error: Enter a valid number!")



title_label = customtkinter.CTkLabel(app, text="Currency Converter", font=("Arial", 18, "bold"))
title_label.pack(pady=10)


optionmenu_var2 = customtkinter.StringVar(value="USD")
optionmenu2 = customtkinter.CTkOptionMenu(app, values=CURRENCIES, variable=optionmenu_var2)
optionmenu2.pack(pady=5, padx=20, fill="x")

optionmenu_var = customtkinter.StringVar(value="EUR")
optionmenu = customtkinter.CTkOptionMenu(app, values=CURRENCIES, variable=optionmenu_var)
optionmenu.pack(pady=5, padx=20, fill="x")


entry = customtkinter.CTkEntry(app, placeholder_text="Amount")
entry.pack(pady=10, padx=20, fill="x")


button = customtkinter.CTkButton(app, text="Convert", command=button_callback)
button.pack(pady=15, padx=20, fill="x")


result_label = customtkinter.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10, padx=20)

app.mainloop()
