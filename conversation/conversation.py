import random

class ConversationOrder:
    def __init__(self, filename="conversation\dialogues_order.txt"):
        self.dialogue = self.load_dialogues(filename)


    def load_dialogues(self, filename):
        """Mətn faylından dialoqu oxuyur."""
        try:
            # Faylı oxuyur və boşluqa görə seçir
            with open(filename, "r", encoding="utf-8") as file:
                dialogues = file.read().split("\n\n")
            return dialogues
        except FileNotFoundError:
            print(f"Error: The file \"{filename}\" was not found.")
            raise


    def order_dialogue(self, *args):
        if len(args) != 5:
            return "Yalnız 5 argument göndərə bilərsiz."

        order, decoration, weight, time, total_price = args

        # Dialoqlardan təsadüfi birini seçirik
        selected_dialogue = random.choice(self.dialogue)

        # Dialoqu yaradıb qaytarırıq
        dialogue = selected_dialogue.format(order=order, 
                                            decoration=decoration, 
                                            weight=weight, 
                                            time=time, 
                                            total_price=total_price
                                            )

        # Dialoqu qaytarırıq
        return dialogue.splitlines()



class ConversationSweets:
    def __init__(self, filename="conversation\dialogues_sweet.txt"):
        self.dialogue = self.load_dialogues(filename)


    def load_dialogues(self, filename):
        """Mətn faylından dialoqu oxuyur."""
        try:
            # Faylı oxuyur və boşluqa görə seçir
            with open(filename, "r", encoding="utf-8") as file:
                dialogues = file.read().split("\n\n") 
            return dialogues
        except FileNotFoundError:
            print(f"Error: The file \"{filename}\" was not found.")
            raise


    def sweet_dialogue(self, *args):
        if len(args) != 3:
            return "Yalnız 3 argument göndərə bilərsiz."

        sweets, weight, total_price = args

        # Dialoqlardan təsadüfi birini seçirik
        selected_dialogue = random.choice(self.dialogue)

        # Dialoqu yaradıb qaytarırıq
        dialogue = selected_dialogue.format(sweets=sweets, 
                                            weight=weight, 
                                            total_price=total_price
                                            )

        # Dialoqu qaytarırıq
        return dialogue.splitlines()


class ConversationCake:
    def __init__(self, filename="conversation\dialogues_cake.txt"):
        self.dialogue = self.load_dialogues(filename)


    def load_dialogues(self, filename):
        """Mətn faylından dialoqu oxuyur."""
        try:
            # Faylı oxuyur və boşluqa görə seçir
            with open(filename, "r", encoding="utf-8") as file:
                dialogues = file.read().split("\n\n")  
            return dialogues
        except FileNotFoundError:
            print(f"Error: The file \"{filename}\" was not found.")
            raise


    def cake_dialogue(self, *args):
        if len(args) != 3:
            return "Yalnız 3 argument göndərə bilərsiz."

        cake, weight, total_price = args

        # Dialoqlardan təsadüfi birini seçirik
        selected_dialogue = random.choice(self.dialogue)

        # Dialoqu yaradıb qaytarırıq
        dialogue = selected_dialogue.format(cake=cake, 
                                            weight=weight, 
                                            total_price=total_price
                                            )

        # Dialoqu qaytarırıq
        return dialogue.splitlines()
    

class ConversationBistro:
    def __init__(self, filename="conversation\dialogues_bistro.txt"):
        self.dialogue = self.load_dialogues(filename)


    def load_dialogues(self, filename):
        """Mətn faylından dialoqu oxuyur."""
        try:
            # Faylı oxuyur və boşluqa görə seçir
            with open(filename, "r", encoding="utf-8") as file:
                dialogues = file.read().split("\n\n")  
            return dialogues
        except FileNotFoundError:
            print(f"Error: The file \"{filename}\" was not found.")
            raise


    def bistro_dialogue(self, *args):
        if len(args) != 4:
            return "Yalnız 3 argument göndərə bilərsiz."

        beverage, sweet, count, total_price = args

        # Dialoqlardan təsadüfi birini seçirik
        selected_dialogue = random.choice(self.dialogue)

        # Dialoqu yaradıb qaytarırıq
        dialogue = selected_dialogue.format(beverage=beverage,
                                            sweet=sweet,
                                            count=count, 
                                            total_price=total_price
                                            )

        # Dialoqu qaytarırıq
        return dialogue.splitlines()