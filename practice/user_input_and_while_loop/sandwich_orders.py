sandwich_orders = ["Black Forest Ham", "Chicken & Bacon Ranch Melt", "Cold Cut Combo"]
finished_orders = []
while sandwich_orders:
    finished_order = sandwich_orders.pop()
    print("I made your " + finished_order)
    finished_orders.append(finished_order)
for finished_order in finished_orders:
    print(finished_order)
