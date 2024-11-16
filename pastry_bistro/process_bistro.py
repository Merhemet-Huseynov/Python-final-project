from pastry_bistro.bistro_functions import BistroFunctions
from table import bistro_add_to_table  
from datetime import datetime
from balance import Balance
from constants import MENU
import random

 
def process_bistro(*args):
    """Bu funksiyaya 5 argument göndərilir. Müştəri, müştərinin pulu, müştərinin verdiyi sifarişin 
             çəkisi, cədvəl yaratmaq üçün funksiya və balans hesablamaq üçün funksiya."""

    if len(args) != 5:
        return f"Yalnız 5 argument daxil edə bilərsiniz."

    # Göndərilən argumentləri pozisiyasına görə götürür
    customer_name, customer_money, customer_order_weight, table, balance = args

    # Obyektlərin yaradılması
    bistro_functions = BistroFunctions()
    menu = MENU()

    # İçkinin adı, maya qiyməti və satış qiyməti 
    beverage_choose, beverage_cost_price, beverage_selling_price = bistro_functions.beverage_details()

    # Şirniyat adı, maya qiyməti və satış qiyməti
    sweet_choose, sweet_cost_price, sweet_selling_price = bistro_functions.sweet_details()

    # Ümumi qiymətin hesablanması və satış tarix
    beverage_total_sell_price = bistro_functions.calculate_order_price(beverage_selling_price, 
                                                                       customer_order_weight
                                                                      )

    sweet_total_sell_price = bistro_functions.calculate_order_price(sweet_selling_price, 
                                                                    customer_order_weight
                                                                    )
    total_price = beverage_total_sell_price + sweet_total_sell_price
    sell_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Müştərinin büdcəsini yoxlayır
    if total_price <= customer_money:

        # Xərcləri hesablayır
        beverage_costs = bistro_functions.calculate_costs(beverage_cost_price,      
                                                          customer_order_weight
                                                          )

        sweet_costs = bistro_functions.calculate_costs(beverage_cost_price,      
                                                       customer_order_weight
                                                      )
        # Ümumi xərc
        total_costs = beverage_costs + sweet_costs

        balance.total_income_balance += total_price       # Ümumi satışlar hesablayır
        balance.exspense_balance += total_costs           # Ümumi xərcləri hesablayır
        balance.net_balance += total_price - total_costs  # Təmiz qazancı hesablayır

        # Satış zamanı dialog
        bistro_functions.bistro_dialogue(beverage_choose,
                                         sweet_choose, 
                                         customer_order_weight, 
                                         total_price
                                         )


        # Cədvəli yaratmaq üçün (bistro_add_to_table) funksiyasını çağırır
        bistro_add_to_table(table, customer_name, beverage_choose, 
                            customer_order_weight, beverage_selling_price, 
                            beverage_total_sell_price, sell_time
                            )

        bistro_add_to_table(table, customer_name, sweet_choose, 
                            customer_order_weight, sweet_selling_price, 
                            sweet_total_sell_price, sell_time
                            )

        
        print(f"\nSifariş:              I {beverage_choose}")
        print(f"Sifarişin sayı:       I {customer_order_weight} ədəd")
        print(f"1 ədədinin qiyməti:   I {beverage_selling_price} m")
        print(f"Sifariş:              I {sweet_choose}")
        print(f"Sifarişin çəkisi:     I {customer_order_weight} ədəd")
        print(f"1 ədədinin qiyməti:   I {sweet_selling_price} m")
        print(f"Ümumi qiymət:         I {sweet_total_sell_price} m")
        print(f"Tarix:                I {sell_time}\n")

        return True
    else:
        # Müştərinin balansı çatmadıqda çap edir.
        print(f"Müştərinin balansında kifayət qədər pul yoxdur.")
        return False