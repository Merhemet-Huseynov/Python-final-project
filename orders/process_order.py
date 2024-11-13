from datetime import datetime
from orders.order_functions import OrderFunctions
from constants import ORDER
from table import add_to_table  
import random


def process_order(*args):
    """Bu funksiyaya 5 argument göndərilir: Müştəri, müştərinin pulu, müştərinin verdiyi sifarişin 
             çəkisi, cədvəl yaratmaq üçün funksiya və balans hesablamaq üçün funksiya."""

    if len(args) != 5:
        return "Yalnız 5 argument daxil edə bilərsiz."

    customer_name, customer_money, customer_order_weight, table, balance = args
        
    # Obyektlərin yaradılması 
    order_functions = OrderFunctions() 
    order = ORDER()

    # Sifarişin adı, maya qiyməti və satış qiyməti
    placing_order, selling_price, yeast_price, backing_time = order_functions.select_order(order)

    # Sifarişin ümumi qiymətini hesablayır
    order_total_sell_price = order_functions.calculate_order_price(selling_price, 
                                                                  customer_order_weight
                                                                  )
    sell_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Balansı yoxlayır
    if order_total_sell_price <= customer_money:
        # Xərcləri və net qazancı hesablayır
        costs = order_functions.calculate_costs(yeast_price, customer_order_weight)

        # Dekorasiyanı seçmək və çap etmək
        decorators = order_functions.cake_decoration()
        order_functions.print_order_dialogue(placing_order, 
                                             decorators, 
                                             customer_order_weight, 
                                             backing_time, 
                                             order_total_sell_price
                                             )


        # Cədvələ əlavə olunması
        add_to_table(table, customer_name, placing_order, customer_order_weight, 
                     selling_price, order_total_sell_price, sell_time
                     )

        # Çek məlumatları
        print(f"\nSifariş:            I {placing_order}")
        print(f"Sifarişin çəkisi:     I {customer_order_weight} kq")
        print(f"Sifarişin 1kq qiymət: I {selling_price} m")
        print(f"Ümumi qiymət:         I {order_total_sell_price} m")
        print(f"Tarix:                I {sell_time}\n")

        return True
    else:
        # Müştərinin büdcəsi çatmadıqda verilən mesaj
        print(f"Müştərinin balansında kifayət qeder pul yoxdur.")
        return False
