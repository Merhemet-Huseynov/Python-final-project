from datetime import datetime
from functions import print_order_dialogue, calculate_order_price, calculate_costs, cake_decoration
from constants import ORDER
from balance import Balance
from prettytable import PrettyTable
import random

def process_order(customer_name, customer_money, customer_order_weight, table, balance):
    order = ORDER()

    # Cədvəlin başlığının yaradılması
    table.field_names = ["Müştəri id",
                         "Aldığı Məhsul", 
                         "Çəki", "1kq qiyməti", 
                         "Sifarişin Qiyməti", 
                         "Tarix"
                         ]

    # Sifarişin seçilməsi, qiymət və hazırlanma vaxtı
    placing_orders = random.choice(list(order.ORDERS_AVİLABLE.keys()))
    order_content = order.ORDERS_AVİLABLE[placing_orders]
    selling_price_order = order_content["Satış qiyməti"]
    yeast_price_order = order_content["Maya qiyməti"]
    backing_time_order = order_content["Hazırlanma vaxtı"]

    # Sifarişin ümumi qiymətini hesablayır
    order_total_sell_price = calculate_order_price(selling_price_order, customer_order_weight)
    sell_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Balansı yoxlayır
    if order_total_sell_price <= customer_money:
        
        # Xərcləri və net qazancı hesablayır 
        balance.total_income_balance += order_total_sell_price
        costs = calculate_costs(yeast_price_order, customer_order_weight)
        balance.exspense_balance += costs
        balance.net_balance += order_total_sell_price - costs

        # Dekorasiyanı seçmək və çap etmək
        decorators = cake_decoration()
        print_order_dialogue(placing_orders, 
                             decorators, 
                             customer_order_weight, 
                             backing_time_order, 
                             order_total_sell_price
                            )

        # Cədvələ məlumat əlavə edirik
        table.add_row([customer_name, 
                       placing_orders, 
                       f"{customer_order_weight} kq", 
                       f"{selling_price_order} $", 
                       f"{order_total_sell_price} $", 
                       sell_time
                       ])

        # Çek məlumatları
        print(f"Sifariş:              I {placing_orders}")
        print(f"Sifarişin çəkisi:     I {customer_order_weight} kq")
        print(f"Sifarişin 1kq qiymət: I {selling_price_order} $")
        print(f"Ümumi qiymət:         I {order_total_sell_price} $")
        print(f"Tarix:                I {sell_time}\n")

        # Sifariş uğurla yerinə yetirildi
        return True  
    else:
        return f"---Müştəri büdcəsinə uyğun olmadığını düşündü, sifariş etməkdən imtina etdi.\n"
