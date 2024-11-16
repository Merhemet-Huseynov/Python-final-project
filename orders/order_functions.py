from conversation.conversation import ConversationOrder
from constants import DECORATIONS
import random
import time

class OrderFunctions:

    # Sifarişin ümumi qiymətini hesablamaq
    def calculate_order_price(self, selling_price, order_weight):
        return selling_price * order_weight


    # Sifarişin xərclərini hesablamaq
    def calculate_costs(self, yeast_price_order, customer_order_weight):
        return yeast_price_order * customer_order_weight


    # Tort üçün random dekorasiyaları seçir
    def cake_decoration(self):
        decorator = DECORATIONS()  
        customer_decoration = random.choice(decorator.POSSIBLE_DECORATIONS)
        return customer_decoration


    # Müştərinin balansını yoxlayıb, lazımi əməliyyatları yerinə yetirir
    def update_balance(self, balance, order_total_sell_price, costs):
        balance.total_income_balance += order_total_sell_price
        balance.exspense_balance += costs
        balance.net_balance += order_total_sell_price - costs


    # Dialoqu Çap Etmək
    def print_order_dialogue(self, placing_orders, decorators,
                             order_weight, backing_time_order, 
                             order_total_sell_price
                             ):
        # Obyekt yaradır    
        conversation_order = ConversationOrder()

        # Sifariş zamanı dialoq yaradır 
        dialogue_customer_seller = conversation_order.order_dialogue(placing_orders,
                                                                     decorators, 
                                                                     order_weight, 
                                                                     backing_time_order, 
                                                                     order_total_sell_price
                                                                    )
        
        for item in dialogue_customer_seller:
            # time.sleep(1.5)
            print(item)


    def select_order(self, order):
        """Bu funksiya təsadüfi olaraq bir sifarişi seçir və onun qiymətini, maya qiymətini 
                         və hazırlanma vaxtını qaytarır."""
                         
        placing_order = random.choice(list(order.ORDERS_AVİLABLE.keys())) 
        order_content = order.ORDERS_AVİLABLE.get(placing_order)
        selling_price = order_content.get("Satış qiyməti", "Satış qiyməti tapılmadı")
        yeast_price = order_content.get("Maya qiyməti", "Maya qiyməti tapılmadı")
        backing_time = order_content.get("Hazırlanma vaxtı")

        return placing_order, selling_price, yeast_price, backing_time
