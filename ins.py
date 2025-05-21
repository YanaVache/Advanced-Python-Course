import requests 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
from matplotlib.ticker import FormatStrFormatter

def get_monthly_data(currency = 'USD', year = 2021):
    
    start_date, end_date = f'{year}-01-01', f'{year}-12-31'
    table_type = 'A'
    headers = {}

    url = f'http://api.nbp.pl/api/exchangerates/rates/{table_type}/{currency}/{start_date}/{end_date}'
    params = {'format' : 'json'}

    r = requests.get(url, params=params, headers=headers)
    data = r.json()['rates']
    data = [(dt.date.fromisoformat(datum['effectiveDate']), datum['mid']) for datum in data]
    
    data_monthly = [[0, 0] for _ in range(0, 12)]
    for d, x in data:
        month = d.month-1
        data_monthly[month][0] += x
        data_monthly[month][1] += 1

    return [sum/total for sum, total in data_monthly]

# some way to predic data (probably a poor prediction)
def predict_data(data_1, data_2):
    return [(x+y)/2 for x, y in zip(data_1, data_2)]

if __name__ == '__main__':
    data2021 = get_monthly_data()
    data2020 = get_monthly_data(year=2020)
    data2022 = predict_data(data2020, data2021)

    plt.figure(figsize=(12, 6))
    plt.title('USD to PLN')
    plt.xlabel('Month')
    plt.ylabel('course')

    # set precision of y axis
    ax = plt.gca()
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    plt.plot(range(0, 12), data2021, label = '2021')
    plt.plot(range(0, 12), data2020, label = '2020')
    plt.plot(range(0, 12), data2022, label = '2022 (prediction)')
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan']
    plt.xticks(range(0, 13), months)   
    plt.legend()
    plt.show()
    