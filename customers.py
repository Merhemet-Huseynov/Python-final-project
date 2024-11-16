import random

class Customers: 
    def __init__(self,):
        self.customers_dict = {} 
    
    # Müştəriləri lüğətə əlavə etmək üçün metod
    def add_customer(self, name, money, weight): 
        self.customers_dict[name] = {"Pulu": money,
                                    "Sifarişin çəkisi": weight
                                     }
    
    # Kodun istifadəçilər tərəfindən daha oxunaqlı olması üçün metod
    def __repr__(self):
        result = []
        
        for name, details in self.customers_dict.items():
            result.append(f"{name}: {details["Sifarişin çəkisi"]}kg")
            
        return "\n".join(result)

    random_customer_count = random.randint(1, 9) 


# Müştəri yaradır, onun pulunu, sifarişin çəkisini, və id-ni yaradır
def create_customer():
    customer_name = f"Müştəri"  
    random_money = random.randint(500, 2000)
    order_weight = random.randint(1, 10)

    # Müştəri obyektini yaratmaq
    customers = Customers()  
    customers.add_customer(customer_name, 
                           random_money, 
                           order_weight
                           )

    return customer_name, random_money, order_weight