class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.spendings = 0      #will sum up all withdrawals
    def __repr__(self):
        return self.title() + "\n" + self.items()

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    #returns true if funds are available
    def check_funds(self, amount):
        if amount > self.get_balance(): return False
        else: return True
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.spendings += amount
            return True
        else: return False

    #shows the total balance after all actions have been done
    def get_balance(self):
        bal = 0
        i = 0
        for action in self.ledger:
            bal += self.ledger[i].get("amount")
            i += 1
        return bal
    def transfer(self, amount, to_category, description = ""):
        if self.check_funds(amount):
            to_category.deposit(amount, "Transfer from " + self.name)
            self.withdraw(amount, "Transfer to " + to_category.name)
            return True
        else: return False

    #only the first line when printing the object
    def title(self):
        asterisk = "*" * int((30 - len(self.name))/ 2)
        if len(self.name) % 2 == 1:
            return asterisk + self.name + asterisk + "*"
        return asterisk + self.name + asterisk

    #lists all the actions/values in the ledger in the proper format
    def items(self):
        format = ""
        total = 0
        for item in self.ledger:
            d = item["description"]
            a = "{:.2f}".format(item["amount"])     #converts to string and shows 2 decimal places
            total += float(item["amount"])
            if len(d) > 23:
                format += d[:23]
            else:
                format += d + " " * (23 - len(d))
            format += " " * (7 - len(a)) + a
            format += "\n"
        format += "Total: " + "{:.2f}".format(total)     #ensures 2 decimal places in total
        return format
def create_spend_chart(categories):
    percents = []
    total = 0
    percent_index = {"100": 1, "90": 2, "80": 3, "70": 4, "60": 5, "50": 6, "40": 7, "30": 8, "20": 9, "10": 10, "0": 11}
    column_index = [6, 9, 12, 15]
    i = 0       #index for the establishing the percent list
    j = 5       #index for establishing what space in the string to replace
    chart = ""
    #col = len(percents)
    for cat in categories:
        percents.append(round(cat.spendings,2))
    for val in percents:
        total += val

    #rounds the percentages spent down to the nearest 10
    for val in percents:
        percents[i] = int(val /total * 100) - (int(val /total * 100) % 10)
        i += 1
    lines = [ "Percentage spent by category",
              "\n100| " + " " * (len(categories) * 3),
              "\n 90| " + " " * (len(categories) * 3),
              "\n 80| " + " " * (len(categories) * 3),
              "\n 70| " + " " * (len(categories) * 3),
              "\n 60| " + " " * (len(categories) * 3),
              "\n 50| " + " " * (len(categories) * 3),
              "\n 40| " + " " * (len(categories) * 3),
              "\n 30| " + " " * (len(categories) * 3),
              "\n 20| " + " " * (len(categories) * 3),
              "\n 10| " + " " * (len(categories) * 3),
              "\n  0| " + " " * (len(categories) * 3),
              "\n    " + "-" * (len(categories) * 3 + 1)]

    #adds the "o"'s in the right spot by comparing percent to every percent key
    for percent in percents:
            for key in percent_index.keys():
                if percent == percents[-1] and int(key) <= percent:
                    lines[percent_index[key]] = lines[percent_index[key]][:column_index[percents.index(percent)]] + "o"
                elif int(key) <= percent:
                    lines[percent_index[key]] = lines[percent_index[key]][:column_index[percents.index(percent)]] + "o  "

    for line in lines:
        #fill in extra spaces at end of chart
        while len(line) < 6 + (len(categories) * 3):
            line += " "
        chart += line

    #get the words to print vertically below the chart
    vertical = ""
    longest = 0
    i = 0  # index for letter in category name
    #need to determine longest category title for max lines for the labels
    for cat in categories:
        if len(cat.name) > longest:
            longest = len(cat.name)
    for x in range(longest):
        vertical += "\n     "
        #goes through the same letter of each category name each iteration
        for c in range(len(categories)):
            #empty spaces when the adjacent category has more letters
            if len(categories[c].name) < longest and x >= len(categories[c].name):
                 vertical += "   "
            else:
                vertical += categories[c].name[i] + "  "
        i += 1
    chart += vertical
    return chart

#part of test
food = Category("Food")
utilities = Category("Utilities")
entertainment = Category("Entertainment")
savings = Category("Savings")
savings.deposit(1000, "deposit")
food.deposit(100, "deposit")
entertainment.deposit(50, "deposit")
utilities.deposit(750, "deposit")
food.withdraw(32.35, "dinner with bestie")
entertainment.withdraw(8, "spotify premium")
entertainment.withdraw(15.49, "netflix")
utilities.withdraw(56.05, "water")
utilities.withdraw(61.98, "electricity")
food.withdraw(49.66, "TJ's haul")
utilities.transfer(250, savings, "idk just cuz")
actual = create_spend_chart([utilities, food, entertainment,savings])
print(actual)
print(food)
print(entertainment)
print(savings)
print(utilities)
