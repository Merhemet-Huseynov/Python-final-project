from conversation.conversation import ConversationBistro
from constants import MENU
import random
import time

class BistroFunctions:

    # Sifarişin ümumi qiymətini hesablamaq
    def calculate_order_price(self, selling_price, cake_weight):
        return selling_price * cake_weight


    # Sifarişin xərclərini hesablamaq
    def calculate_costs(self, yeast_price_cake, customer_order_weight):
        return yeast_price_cake * customer_order_weight


    # Dialoqu Çap Etmək
    def bistro_dialogue(self, *args):
                
        if len(args) != 4:
            return "Yalnız 4 argument daxil edə bilərsiz."
        
        beverage, sweet, count, total_price = args
        
        # Obyekt yaradır    
        conversation_bistro = ConversationBistro()
        
        # Sifariş zamanı dialoq yaradır 
        dialogue_customer_seller = conversation_bistro.bistro_dialogue(beverage,
                                                                       sweet,
                                                                       count,
                                                                       total_price
                                                                       )
        for item in dialogue_customer_seller:
            time.sleep(1.5)
            print(item)


    def beverage_details(self):
        "İçkiler haqqında məlumat. Maya qiyməti, satış qiyməti"

        random_beverage = random.choice(list(MENU.BEVERAGES.keys()))
        beverage_details = MENU.BEVERAGES[random_beverage]
        beverage_yeast_price = beverage_details.get("Maya Dəyəri")
        beverage_seling_price = beverage_details.get("Satış Qiyməti")

        return random_beverage, beverage_yeast_price, beverage_seling_price


    def sweet_details(self):
        "Şirniyatlar haqqında məlumat. Maya qiyməti, satış qiyməti"

        random_sweet = random.choice(list(MENU.SWEETS_MENU.keys()))
        sweet_details = MENU.SWEETS_MENU[random_sweet]
        sweet_yeast_price = sweet_details.get("Maya Dəyəri")
        sweet_seling_price = sweet_details.get("Satış Qiyməti")

        return random_sweet, sweet_yeast_price, sweet_seling_price