import random
import time
from constants import SWEETS
from conversation.conversation import ConversationSweets

class SweetsFunctions:

    # Sifarişin ümumi qiymətini hesablamaq
    def calculate_sweets_price(self, selling_price, order_weight):
        return selling_price * order_weight


    # Sifarişin xərclərini hesablamaq
    def calculate_costs(self, yeast_price_sweets, customer_order_weight):
        return yeast_price_sweets * customer_order_weight


    # Dialoqu çap etmək
    def sweets_selling_dialogue(self, *args):
                
        if len(args) != 3:
            return "Yalnız 3 argument daxil edə bilərsiz."
        
        sweets, weight, total_price = args
        
        # Obyekt yaradır    
        conversation_sweets = ConversationSweets()
        
        # Sifariş zamanı dialoq yaradır 
        dialogue_customer_seller = conversation_sweets.sweet_dialogue(sweets,
                                                                      weight, 
                                                                      total_price, 
                                                                      )
        for item in dialogue_customer_seller:
            time.sleep(1.5)
            print(item)


    def sweets_detalis(self):
        """Bu funksiya təsadüfi olaraq bir şirniyat seçir və onun qiymətini, maya qiymətini 
                         və hazırlanma vaxtını qaytarır."""

        sweets_choose = random.choice(list(SWEETS.SWEETS_AVELIABLE.keys()))
        sweets_kind = SWEETS.SWEETS_AVELIABLE.get(sweets_choose) 
        sweets_cost_price = sweets_kind.get("Maya dəyəri")
        sweets_selling_price = sweets_kind.get("Satış qiymət")

        return sweets_choose, sweets_cost_price, sweets_selling_price