class currency:
    def __init__(self, money):
        self.money = money

    def __format__(self, format_spec):
        if format_spec == "pounds":
            return f"You have £{self.money:.2f}"
        elif format_spec == "pence":
            return f"You have {self.money * 100:.0f}p"


Syed = currency(21.3532)

print(f"{Syed:pounds}")
print(f"{Syed:pence}")


