class Employee:
    def __init__(self):
        self.income = 0
    
    def earn_money(self, money):
        self.income += money

    @property   #使用property decorator，讓程式更有可讀性
    def tax_amount(self):   # 並不是真真的property (虛擬的)
        return self.income * 0.05
    
    @tax_amount.setter   # 這個方法是用來設定property的值
    def tax_amount(self, tax_number):
        self.income = tax_number / 0.05


wilson = Employee()
wilson.earn_money(300)
print(wilson.tax_amount)  # 15.0 tax_amount virtual property is read-only

wilson.tax_amount = 200
print(wilson.income)  # 4000.0