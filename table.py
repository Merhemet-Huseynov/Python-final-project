from prettytable import PrettyTable

def add_to_table(*args):
    table, customer, product_choose, product_weight, cost_price, total_price, sell_time = args
    # Cədvəl başlığı yaradır
    table.field_names = [
        "Müştəri", 
        "Aldığı Məhsul", 
        "Çəki", 
        "1kq qiyməti", 
        "Sifarişin Qiyməti", 
        "Tarix"
    ]
    
    # Sətirlərini əlavə edir
    table.add_row([
        customer, 
        product_choose, 
        f"{product_weight} kq", 
        f"{cost_price} m", 
        f"{total_price} m", 
        sell_time
    ])