from sweets.process_selling_sweets import process_selling_sweets
from cakes.process_selling_cake import process_selling_cakes
from pastry_bistro.process_bistro import process_bistro
from orders.process_order import process_order 
from customers import create_customer
from prettytable import PrettyTable
from file import save_to_file
from balance import Balance
import datetime
import time
import random

# Obyektlərin yaradılması
balance = Balance()
table = PrettyTable()

# Müştəri sayını təyin edir
random_customer_count = random.randint(1, 2) 

# Dövrün başlanğıc və son vaxtı
start_time = datetime.datetime.now()
end_time = start_time + datetime.timedelta(minutes=5)

# 5 dəqiqə dövr edecek
while datetime.datetime.now() < end_time:
    # Müştərilər üçün ümumi satış prosesini icra edən funksiya
    def process_customer_sales(process_function):
        for _ in range(random_customer_count):
            # Müştəri haqqında məlumatları alırıq
            customer_name, customer_money, customer_order_weight = create_customer()
            
            # Müştəriyə uyğun satış prosesini başlatmaq
            process_function(customer_name, 
                            customer_money, 
                            customer_order_weight, 
                            table, 
                            balance
                            )

    # Satış proseslərini funksiyalarla gönderirik
    process_customer_sales(process_order)
    process_customer_sales(process_selling_sweets)
    process_customer_sales(process_selling_cakes)
    process_customer_sales(process_bistro)

    # Hər dövr arasında 1.5 saniya 
    time.sleep(1.5)

# Balans məlumatlarını fayla saxlayırıq
total_income_balance = balance.total_income_balance
exspense_balance = balance.exspense_balance
net_balance = balance.net_balance
result = save_to_file(table, total_income_balance, exspense_balance, net_balance)


if __name__ == "__main":
    # Cədvəli və balansı çap edirik
    print(table)
    print(f"Ümumi qazanc: {balance.total_income_balance} m")
    print(f"Xərclər: {balance.exspense_balance} m")
    print(f"Net qazanc: {balance.net_balance} m")
    print(result)

print("Satış hesabatı (sales_report.txt) faylında saxlandı")