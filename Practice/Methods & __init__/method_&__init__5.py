class Mobile:
    def __init__(self, brand, model, price = 10000):
        self.brand = brand
        self.model = model
        self.price = price
    
    def info(self):
        print("Brand:", self.brand, "Model:", self.model, "Price:", self.price)

b1 = Mobile("Vivo", "V30")
b2 = Mobile("MI", "Redmi note 14 pro 5G", 100000)
b1.info()
b2.info()