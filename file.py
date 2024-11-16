def save_to_file(*args):

    table, total_income_balance, expense_balance, net_balance = args
    
    with open("sales_report.txt", "w", encoding="utf-8") as f:
        f.write("Satış Hesabatı\n")
        f.write("---------------\n")
        f.write(str(table))
        f.write("\nÜmumi gəlir: " + str(total_income_balance) + " m\n")
        f.write(f"Xərclər: {expense_balance} m\n") 
        f.write(f"Net qazanc: {net_balance} m\n\n")

    return ("Satış hesabatı burada saxlanıldı: sales_report.txt")

