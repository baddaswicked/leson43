class Cafe:
    def __init__(self):
        self.menu={
            "чай":10,
            "кава":15,
            "какао":10,
            "лате":15
        }
        self.orders=[]

    def __call__(self, item=str, quantity=1):
        if item.lower() in self.menu:
            total_price=self.menu[item.lower()]*quantity
            self.orders.append((item.lower(),quantity,total_price))
            print(f"Замовлення {quantity} {item.lower()}. Загальна ціна: {total_price}грн")
        else:
            print("Вибачте такого напою немає!")

    def show_order(self):
        if self.orders:
            print("Ваші замовлення")
            for order in self.orders:
                print(f"{order[1]} * {order[0]} = {order[2]} ")
            print(f"Загальна ціна замовлення {self.all_price()}")
        else:
            print("У вас немає замовлень")
    def all_price(self):
        price=0
        for order in self.orders:
            price+=order[2]
        return price

cafe=Cafe()
cafe("Чай",3)
cafe("какао")
cafe("еспресо")
cafe.show_order()