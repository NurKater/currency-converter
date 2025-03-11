import requests
import customtkinter

customtkinter.set_appearance_mode("system")

app = customtkinter.CTk()
app.geometry("300x300")
app.minsize(300, 300)

BASE_URL = "https://api.exchangerate-api.com/v4/latest/"

def convert_currency(amount, from_currency, to_currency):
    url = f"{BASE_URL}{from_currency}"
    response = requests.get(url)
    rates = response.json()["rates"]
    target_rate = rates[to_currency]
    converted = target_rate * amount
    return round(converted, 2)

def button_callback():
    try:
        amount = float(entry.get())
        from_currency = optionmenu_var2.get()
        to_currency = optionmenu_var.get()
        result = convert_currency(amount, from_currency, to_currency)
        result_label.configure(text=f"Converted: {amount} {from_currency} = {result} {to_currency}")
    except ValueError:
        result_label.configure(text="Error: Enter a valid number!")

optionmenu_var2 = customtkinter.StringVar(value="USD")
optionmenu2 = customtkinter.CTkOptionMenu(app,
    values=[
        "USD", "EUR", "UAH", "GBP", "JPY", "CNY", "CHF", "CAD", "AUD", "NZD",
        "SEK", "NOK", "DKK", "PLN", "HUF", "CZK", "SGD", "HKD", "KRW", "INR",
        "BRL", "MXN", "ZAR", "TRY", "RUB", "THB", "IDR", "MYR", "PHP"
    ],
    variable=optionmenu_var2
)
optionmenu2.pack(pady=10, padx=20, fill="x")

optionmenu_var = customtkinter.StringVar(value="USD")
optionmenu = customtkinter.CTkOptionMenu(app,
    values=[
        "USD", "EUR", "UAH", "GBP", "JPY", "CNY", "CHF", "CAD", "AUD", "NZD",
        "SEK", "NOK", "DKK", "PLN", "HUF", "CZK", "SGD", "HKD", "KRW", "INR",
        "BRL", "MXN", "ZAR", "TRY", "RUB", "THB", "IDR", "MYR", "PHP"
    ],
    variable=optionmenu_var
)
optionmenu.pack(pady=10, padx=20, fill="x")

entry = customtkinter.CTkEntry(app, placeholder_text="Amount")
entry.pack(pady=10, padx=20, fill="x")

button = customtkinter.CTkButton(app, text="Convert", command=button_callback)
button.pack(pady=20, padx=20, fill="x")

result_label = customtkinter.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10, padx=20)

app.mainloop()