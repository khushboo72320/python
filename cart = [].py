cart = []

while True:
    print("\n1. Add Item")
    print("2. Show Total")
    print("3. Checkout")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart.append([item, price])
        print(item, "added to cart")

    elif choice == 2:
        total = 0
        print("\nItems in cart:")
        for i in cart:
            print(i[0], "-", i[1])
            total += i[1]

        print("Total =", total)

    elif choice == 3:
        total = 0
        for i in cart:
            total += i[1]

        print("Checkout complete")
        print("Pay amount:", total)
        break

    elif choice == 4:
        print("Exit")
        break

    else:
        print("Invalid choice") 