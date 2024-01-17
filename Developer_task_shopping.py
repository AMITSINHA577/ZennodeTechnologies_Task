prices = {"Product A": 20, "Product B": 40, "Product C": 50}

cart = {}
for product, price in prices.items():
    quantity = int(input(f"Enter quantity for {product}: "))
    gifted = input(f"Is {product} gift wrapped? (yes/no): ").lower() == "yes"
    cart[product] = {"quantity": quantity, "price": price, "gifted": gifted}

subtotal = sum(item["quantity"] * item["price"] for item in cart.values())
gift_wrap_fee = sum(1 * item["quantity"] for item in cart.values() if item["gifted"])
shipping_fee = (sum(item["quantity"] for item in cart.values()) // 10 + 1) * 5

best_discount = 0
best_name = ""
if subtotal > 200:
    best_discount = 10
    best_name = "Flat $10 discount"
elif subtotal > 20:
    best_discount = subtotal * 0.1
    best_name = "10% bulk discount"
for product, item in cart.items():
    if item["quantity"] > 10:
        best_discount = max(best_discount, item["quantity"] * item["price"] * 0.05)
        best_name = "5% bulk discount"

total = subtotal - best_discount + shipping_fee + gift_wrap_fee
print("\nInvoice:")
for product, item in cart.items():
    print(f"{product}: {item['quantity']} units * ${item['price']:.2f} = ${item['quantity'] * item['price']:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount applied: {best_name} (${best_discount:.2f})")
print(f"Shipping fee: ${shipping_fee:.2f}")
print(f"Gift wrap fee: ${gift_wrap_fee:.2f}")
print(f"Total: ${total:.2f}")
