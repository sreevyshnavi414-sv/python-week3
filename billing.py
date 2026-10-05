class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def get_total(self):
        return self.price * self.quantity
class Bill:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.get_total()
        return total
    def calculate_tax(self, total):
        return total * 0.18
    def display_bill(self):
        total = self.calculate_total()
        tax = self.calculate_tax(total)
        final_total = total + tax
        print("\n" + "=" * 60)
        print("                    FINAL BILL")
        print("=" * 60)
        print(f"{'Product':<20}{'Price':<12}{'Qty':<8}{'Amount':<15}")
        print("-" * 60)
        for product in self.products:
            amount = product.get_total()
            print(f"{product.name:<20}{product.price:<12.2f}{product.quantity:<8}{amount:<15.2f}")
        print("-" * 60)
        print(f"{'Subtotal':<40} ₹{total:.2f}")
        print(f"{'Tax (18%)':<40} ₹{tax:.2f}")
        print(f"{'Final Total':<40} ₹{final_total:.2f}")
        print("=" * 60)
bill = Bill()
n = int(input("Enter number of products: "))
for i in range(n):
    print(f"\nProduct {i + 1}")
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    product = Product(name, price, quantity)
    bill.add_product(product)
bill.display_bill()