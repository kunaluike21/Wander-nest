import requests

def get_exchange_rate(from_currency, to_currency):
    api_key = 'YOUR_API_KEY'  # Replace with your own API key
    url = f'https://open.er-api.com/v6/latest/{from_currency}'
    response = requests.get(url)
    data = response.json()
    return data['rates'][to_currency]

def convert_currency(amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

if __name__ == '__main__':
    amount = float(input("Enter amount: "))
    from_currency = input("Enter from currency (e.g., USD): ")
    to_currency = input("Enter to currency (e.g., EUR): ")
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
