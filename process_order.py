from functions import OrderFunctions
from prettytable import PrettyTable
from datetime import datetime
from constants import ORDER
from balance import Balance
import random


def process_order(*args):
    if len(args) != 5:
        return f"Yalnız 5 argument daxil ede bilərsiz."

    customer_name, customer_money, customer_order_weight, table, balance = args
        
    # Obyektlərin yaradılması 
    order_functions = OrderFunctions() 
    order = ORDER()

    # Cədvəlin başlığının yaradılması
    table.field_names = ["Müştəri id", 
                         "Aldığı Məhsul", 
                         "Çəki", 
                         "1kq qiyməti", 
                         "Sifarişin Qiyməti", 
                         "Tarix"
                        ]

    # Sifarişin seçilməsi, qiymət və hazırlanma vaxtı
    placing_order = random.choice(list(order.ORDERS_AVİLABLE.keys())) 
    order_content = order.ORDERS_AVİLABLE.get(placing_order)
    selling_price = order_content.get("Satış qiyməti", "Satış qiyməti tapılmadı")
    yeast_price = order_content.get("Maya qiyməti", "Maya qiyməti tapılmadı")
    backing_time = order_content.get("Hazırlanma vaxtı")


    # Sifarişin ümumi qiymətini hesablayır
    order_total_sell_price = order_functions.calculate_order_price(selling_price, 
                                                                   customer_order_weight
                                                                   )
    sell_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    # Balansı yoxlayır
    if order_total_sell_price <= customer_money:

        # Xərcləri və net qazancı hesablayır
        balance.total_income_balance += order_total_sell_price
        costs = order_functions.calculate_costs(yeast_price, customer_order_weight)
        balance.exspense_balance += costs
        balance.net_balance += order_total_sell_price - costs

        # Dekorasiyanı seçmək və çap etmək
        decorators = order_functions.cake_decoration()
        order_functions.print_order_dialogue(placing_order, 
                                             decorators, 
                                             customer_order_weight, 
                                             backing_time, 
                                             order_total_sell_price
                                             )

        # Cədvələ məlumat əlavə edirik
        table.add_row([customer_name, 
                       placing_order, 
                       f"{customer_order_weight} kq", 
                       f"{selling_price} $", 
                       f"{order_total_sell_price} $", 
                       sell_time
                       ])

        # Çek məlumatları
        print(f"Sifariş:              I {placing_order}")
        print(f"Sifarişin çəkisi:     I {customer_order_weight} kq")
        print(f"Sifarişin 1kq qiymət: I {selling_price} $")
        print(f"Ümumi qiymət:         I {order_total_sell_price} $")
        print(f"Tarix:                I {sell_time}\n")

        # Sifariş uğurla yerinə yetirildi
        return True  
    else:
        # Müştərinin büdcəsi çatmadıqda verilən mesaj
        print(f"Müştərinin balansında kifayət qeder pul yoxdur.")
        return False