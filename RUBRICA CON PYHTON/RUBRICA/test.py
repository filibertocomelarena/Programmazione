class VendingMachine:
    def __init__(self, numero_oggetti, prezzo_degli_oggetti):
        self.num_items = int(numero_oggetti)
        self.item_price = int(prezzo_degli_oggetti)

    def Buy(self, req_items, money):
        if req_items > self.num_items:
            print('Not enough items in the machine')
        if req_items * self.item_price > money:
            print('Not enough money in the machine')
        else:
            return self.num_items - req_items


cazzomacchina = VendingMachine(12,350)
cazzomacchina.Buy(2,1545)
