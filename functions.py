from conversation import order_dialogue
from prettytable import PrettyTable
from constants import DECORATIONS
import random
import time

# Funksiya: Sifarişin Ümumi Qiymətini Hesablamaq
def calculate_order_price(selling_price_order, customer_order_weight):
    return selling_price_order * customer_order_weight


# Funksiya: Sifarişin Xərclərini Hesablamaq
def calculate_costs(yeast_price_order, customer_order_weight):
    return yeast_price_order * customer_order_weight


# Tort üçün random dekorasiyaları seçir
def cake_decoration():
    decorator = DECORATIONS()
    customer_decoration = random.choice(decorator.POSSIBLE_DECORATIONS)
    return customer_decoration


# Funksiya: Dialoqu Çap Etmək
def print_order_dialogue(*args):
        
    placing_orders, decorators, order_weight, backing_time_order, order_total_sell_price = args
    dialogue_customer_seller = order_dialogue(placing_orders,
                                              decorators, 
                                              order_weight, 
                                              backing_time_order, 
                                              order_total_sell_price
                                              )
    for x in dialogue_customer_seller:
        time.sleep(2)
        print(x)
