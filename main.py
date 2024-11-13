from cakes.process_selling_cake import process_selling_cakes
from sweets.process_selling_sweets import process_selling_sweets
from orders.process_order import process_order 
from customers import create_customer
from prettytable import PrettyTable
from balance import Balance
import random

# Obyektlərin yaradılması
balance = Balance()
table = PrettyTable()

# Müştəri sayını təyin edir
random_customer_count = random.randint(1, 2) 


# Müştəri sayı qədər dövür edir.
for x in range(random_customer_count):

    # (creat_customer) funk-unu çağırır, müştəri haqqında
    customer_name, customer_money, customer_order_weight = create_customer()

    # Satış prosesini başlatmaq üçün (process_order) funksiyasını çağırırıq
    process_order(customer_name, 
                  customer_money, 
                  customer_order_weight, 
                  table, 
                  balance
                  )



for x in range(random_customer_count):
    # (creat_customer) funk-unu çağırır, müştəri haqqında
    customer_name, customer_money, customer_order_weight = create_customer()

    # Satış prosesini başlatmaq üçün (process_selling_sweets) funksiyasını çağırırıq
    process_selling_sweets(customer_name, 
                          customer_money, 
                          customer_order_weight, 
                          table, 
                          balance
                          )


for x in range(random_customer_count):

    # (creat_customer) funk-unu çağırır, müştəri haqqında
    customer_name, customer_money, customer_order_weight = create_customer()

    # Satış prosesini başlatmaq üçün (process_selling_cakes) funksiyasını çağırırıq
    process_selling_cakes(customer_name, 
                          customer_money, 
                          customer_order_weight, 
                          table, 
                          balance
                          )


# Cədvəli və balansı çap edirik
print(table)
print(f"Ümumi qazanc: {balance.total_income_balance} m")
print(f"Xərclər: {balance.exspense_balance} m")
print(f"Net qazanc: {balance.net_balance} m")