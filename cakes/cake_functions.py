from conversation.conversation import ConversationCake
from constants import CAKE
import random
import time

class CakeFunctions:

    # Sifarişin ümumi qiymətini hesablamaq
    def calculate_cake_price(self, selling_price, cake_weight):
        return selling_price * cake_weight


    # Sifarişin xərclərini hesablamaq
    def calculate_costs(self, yeast_price_cake, customer_order_weight):
        return yeast_price_cake * customer_order_weight


    # Dialoqu Çap Etmək
    def cake_selling_dialogue(self, *args):
                
        if len(args) != 3:
            return "Yalnız 3 argument daxil edə bilərsiz."
        
        cake, weight, total_price = args
        
        # Obyekt yaradır    
        conversation_cake = ConversationCake()
        
        # Sifariş zamanı dialoq yaradır 
        dialogue_customer_seller = conversation_cake.cake_dialogue(cake,
                                                                   weight, 
                                                                   total_price
                                                                   )
        for item in dialogue_customer_seller:
            time.sleep(1.5)
            print(item)


    def cake_details(self):
        """Bu funksiya təsadüfi olaraq bir sifarişi seçir və onun qiymətini, maya qiymətini 
                         və hazırlanma vaxtını qaytarır."""
        # Obyektləri yaradın
        cake = CAKE()

        # Tort seçimi maya və satış qiymətləri
        cake_choose = random.choice(list(cake.CAKE_AVELIABLE.keys()))
        cake_kind = cake.CAKE_AVELIABLE.get(cake_choose)
        cake_cost_price = cake_kind.get("Maya dəyəri")
        cake_selling_price = cake_kind.get("Satış qiymət")

        return cake_choose, cake_cost_price, cake_selling_price