class Balance:
    def __init__(self):
        self.exspense_balance = 0     # Məhsulun hazırlanmasına sərf olunan xərclər
        self.total_income_balance = 0 # Ümumi gəlir
        self.net_balance = 0          # Net(təmiz) qazanc                       #
        
    def __str__(self):
        return f"Ümumi gəlir: {self.total_income_balance}, \nXərclər: {self.exspense_balance}, \nQazanc: {self.net_balance}"