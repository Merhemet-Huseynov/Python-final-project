from process_order import process_order  
from customers import create_customer
from balance import Balance
from prettytable import PrettyTable
import random

# Obyektlərin yaradılması
balance = Balance()
table = PrettyTable()

# Müştəri sayı
random_customer_count = random.randint(1, 2)

# Müştəri və sifarişlər haqqında məlumat
for x in range(random_customer_count):
    customer_name, customer_money, customer_order_weight = create_customer()

    # Satış prosesini başlatmaq üçün (process_order) funksiyasını çağırırıq
    process_order(customer_name, customer_money, customer_order_weight, table, balance)

# Cədvəli və balansı çap edirik
print(table)
print(f"Ümumi qazanc: {balance.total_income_balance}$")
print(f"Xərclər: {balance.exspense_balance}$")
print(f"Net qazanc: {balance.net_balance}$")
