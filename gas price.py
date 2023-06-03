from collections import defaultdict

def get_price(str):
    items = str.split(':')
    return float(items[1])

def get_month(str):
    items = str.split('-')
    return int(items[0])
def get_year(str):
    items = str.split(':')
    date_items = items[0].split('-')
    return int(date_items[2])

def monthly_average(gas_list):
    month_names = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    monthly_prices = defaultdict(list)
    for gas in gas_list:
        month = get_month(gas)
        monthly_prices[month].append(get_price(gas))

    for month, prices in monthly_prices.items():
        average = sum(prices) / len(prices) 
        year = get_year(gas_list[0])
        print(f'Average price for {month_names[month-1]}),{year}: ${average:.2f} ')


def main():
    gas_file = open(r"C:\Users\Ada\Downloads\Gaspricing.txt", "r")
    gas_list = gas_file.readlines()
    
    monthly_average(gas_list)


main()