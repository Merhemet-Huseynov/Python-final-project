from conversation import Conversation
from prettytable import PrettyTable
from constants import DECORATIONS
import random
import time

class OrderFunctions:

    # Sifarişin ümumi qiymətini hesablamaq
    def calculate_order_price(self, selling_price, order_weight):
        return selling_price * order_weight


    # Sifarişin Xərclərini Hesablamaq
    def calculate_costs(self, yeast_price_order, customer_order_weight):
        return yeast_price_order * customer_order_weight


    # Tort üçün random dekorasiyaları seçir
    def cake_decoration(self):
        decorator = DECORATIONS()
        customer_decoration = random.choice(decorator.POSSIBLE_DECORATIONS)
        return customer_decoration


    # Dialoqu Çap Etmək
    def print_order_dialogue(self, *args):
                
        if len(args) !=5:
            return "Yalnız 5 argument daxil edə bilərsiz."
        
        placing_orders, decorators, order_weight, backing_time_order, order_total_sell_price = args
        
        # Obyekt yaradır    
        conversation = Conversation()
        
        # Sifariş zamanı dialoq yaradır 
        dialogue_customer_seller = conversation.order_dialogue(placing_orders,
                                                               decorators, 
                                                               order_weight, 
                                                               backing_time_order, 
                                                               order_total_sell_price
                                                               )
        for x in dialogue_customer_seller:
            time.sleep(1)
            print(x)