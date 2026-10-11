class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        
    def __str__(self):
        header = self.category.center(30,"*")  
        lines = ""
        for entry in self.ledger:
            description = entry['description'][:23]
            amount = entry["amount"]
            amount = f"{amount:.2f}"[:7]
            out = description + amount.rjust(30-len(description)) + f"\n"
            lines += out 
        total = f"Total: {self.get_balance()}"
        return f"{header}\n{lines}{total}"
        
    def get_balance(self):
        total = 0
        for entry in self.ledger:
            total += entry["amount"]
        return total
        
    def check_funds(self,amount):
        if amount <= self.get_balance():
            return True
        else:
            return False
        

    def deposit(self, amount, description=""):
        self.ledger.append(
            {'amount':amount,'description':description}
        )
    def withdraw(self, amount, description=""):
        total = self.get_balance()
        if self.check_funds(amount):
            neg_amt = amount * -1
            self.ledger.append(
                {'amount': neg_amt,'description': description}
            )
            return True
        else:
            print('Not enough funds')
            return False

    def transfer(self,amount,destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.category}")
            destination.deposit(amount,f"Transfer from {self.category}")
            return True
        else:
            return False

def create_spend_chart(categories):
    title = "Percentage spent by category" 
    cat_prices= []
    total = 0
    for cat in categories:
        amount = 0
        for entry in cat.ledger:
            if entry["amount"] < 0:
                amount += -entry["amount"]
        total += amount

        cat_prices.append({"name":cat.category,"amount":amount,"percent":None})   
    percent_left = 100
    for cat in cat_prices:
        cat["percent"] = (cat["amount"]/total * 100)//10 * 10
    
    line1 = ""
    for i in range(10,-1,-1):
        percent = i*10
        cline = (f"{percent}|").rjust(4) + " "
        for cat in cat_prices:
            if cat["percent"] >= percent:
                cline += "o  "
            else:
                cline += "   "
        print(len(cline))
        line1 += f"{cline}\n"

    bar = "    " + "-" * (len(cat_prices) * 3 + 1)
    max_length = max(len(entry["name"]) for entry in cat_prices)

    line2 = ""
    for i in range(max_length):
        cline = "".rjust(4)+" "
        for cat in cat_prices:
            if i < len(cat["name"]):
                letter = cat["name"][i]
                cline += f"{letter}  "
            else:
                cline += "   "
        line2 += f"{cline}\n"
    return (f"{title}\n{line1}{bar}\n{line2}".rstrip("\n"))



food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

clothing = Category("clothing")
clothing.deposit(500, "deposit")
clothing.withdraw(300,"f")

print(create_spend_chart([food,clothing]))