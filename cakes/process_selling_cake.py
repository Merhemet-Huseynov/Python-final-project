from cakes.cake_functions import CakeFunctions
from table import add_to_table  
from datetime import datetime
from balance import Balance
from constants import CAKE
import random

 
def process_selling_cakes(*args):
    """Bu funksiyaya 5 argument göndərilir. Müştəri, müştərinin pulu, müştərinin verdiyi sifarişin 
             çəkisi, cədvəl yaratmaq üçün funksiya və balans hesablamaq üçün funksiya."""

    if len(args) != 5:
        return f"Yalnız 5 argument daxil edə bilərsiniz."

    # Göndərilən argumentləri pozisiyasına görə götürür
    customer_name, customer_money, customer_order_weight, table, balance = args

    # Obyektlərin yaradılması
    cake_functions = CakeFunctions()
    cake = CAKE()

    # Tortun adı, maya qiyməti və satış qiyməti 
    cake_choose, cake_cost_price, cake_selling_price = cake_functions.cake_details()

    # Ümumi qiymətin hesablanması və satış tarix
    cake_total_sell_price = cake_functions.calculate_cake_price(cake_selling_price, 
                                                                customer_order_weight
                                                                )
    sell_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Müştərinin büdcəsini yoxlayır
    if cake_total_sell_price <= customer_money:
        # Xərclər hesablayır
        costs = cake_functions.calculate_costs(cake_cost_price,      
                                               customer_order_weight
                                               )
        
        balance.total_income_balance += cake_total_sell_price        # Ümumi satışlar hesablayır
        balance.exspense_balance += costs                            # Ümumi xərcləri hesablayır
        balance.net_balance += cake_total_sell_price - costs         # Təmiz qazancı hesablayır

        # Satış zamanı dialog
        cake_functions.cake_selling_dialogue(cake_choose, 
                                            customer_order_weight, 
                                            cake_total_sell_price
                                            )


        # Cədvəli yaratmaq üçün (add_to_table) funksiyasını çağırır
        add_to_table(table, customer_name, cake_choose, 
                     customer_order_weight, cake_selling_price, 
                     cake_total_sell_price, sell_time
                     )

        # Çek yaradır.
        print(f"\nSifariş:              I {cake_choose}")
        print(f"Sifarişin çəkisi:     I {customer_order_weight} kq")
        print(f"Sifarişin 1kq qiymət: I {cake_cost_price} m")
        print(f"Ümumi qiymət:         I {cake_total_sell_price} m")
        print(f"Tarix:                I {sell_time}\n")

        return True
    else:
        # Müştərinin balansı çatmadıqda çap edir.
        print(f"Müştərinin balansında kifayət qədər pul yoxdur.")
        return False
