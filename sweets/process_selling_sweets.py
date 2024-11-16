from datetime import datetime
from sweets.sweet_function import SweetsFunctions
from constants import SWEETS
from balance import Balance
from table import add_to_table  
import random


def process_selling_sweets(*args):
    if len(args) != 5:
        return f"Yalnız 5 argument daxil ede bilərsiz."

    customer_name, customer_money, customer_order_weight, table, balance = args
    
    # Obyektlərin yaradılması 
    sweets_functions = SweetsFunctions() 
    sweets = SWEETS()

    # Şirniyatın adı, maya qiyməti və satış qiyməti 
    sweets_choose, sweets_cost_price, sweets_selling_price = sweets_functions.sweets_detalis()

    # Sifarişin ümumi qiymətini hesablayır
    sweet_total_sell_price = sweets_functions.calculate_sweets_price(sweets_selling_price, 
                                                                     customer_order_weight
                                                                    )
    sell_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 
    # Balansı yoxlayır
    if sweet_total_sell_price <= customer_money:
        
        # Xərcləri hesablayır
        costs = sweets_functions.calculate_costs(sweets_cost_price, 
                                                 customer_order_weight
                                                 )

        balance.total_income_balance += sweet_total_sell_price # Ümumi satışlar hesablayır
        balance.exspense_balance += costs                      # Ümumi xərcləri hesablayır
        balance.net_balance += sweet_total_sell_price - costs  # Təmiz qazancı hesablayır

        # Dialoq seçmək və çap etmək
        sweets_functions.sweets_selling_dialogue(sweets_choose, 
                                                 customer_order_weight,  
                                                 sweet_total_sell_price
                                                )

 
        # Cədvələ əlavə olunması
        add_to_table(table, customer_name, sweets_choose, 
                     customer_order_weight, sweets_selling_price, 
                     sweet_total_sell_price, sell_time
                    )

        # Çek məlumatları
        print(f"\nSifariş:              I {sweets_choose}")
        print(f"Sifarişin çəkisi:     I {customer_order_weight} kq")
        print(f"Sifarişin 1kq qiymət: I {sweets_selling_price} m")
        print(f"Ümumi qiymət:         I {sweet_total_sell_price} m")
        print(f"Tarix:                I {sell_time}\n")

        return True  
    else:
        # Müştərinin büdcəsi çatmadıqda verilən mesaj
        print(f"Müştərinin balansında kifayət qeder pul yoxdur.")
        return False