class Balance:
    def __init__(self):
        self.exspense_balance = 0      # Məhsulun hazırlanmasına sərf olunan xərclər
        self.total_income_balance = 0  # Ümumi gəlir
        self.net_balance = 0           # Net(təmiz) qazanc                       
        

    def __str__(self):
        return (f"Ümumi gəlir: {self.total_income_balance} $\n"
                f"Xərclər: {self.exspense_balance} $\n"
                f"Qazanc: {self.net_balance} $"
                )


    # Xərcləri hesablamaq
    def add_expense(self, amount):
        self.exspense_balance += amount
        self.calculate_net_balance()      


    # Ümumi gəliri hesablamaq
    def add_income(self, amount):
        self.total_income_balance += amount
        self.calculate_net_balance()  


    # Net balansı hesablayır
    def calculate_net_balance(self):
        self.net_balance = self.total_income_balance - self.exspense_balance


    # Balansı sıfırlamaq (istəyə bağlı olaraq)
    def reset(self):
        self.exspense_balance = 0
        self.total_income_balance = 0
        self.net_balance = 0