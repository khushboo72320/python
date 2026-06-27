temperature=[19,23,45,43,42,46]
cold_days=[]
hot_days=[]
for t in temperature:
    if t <=20:
        cold_days.append(t)
    elif t>=20:
        hot_days.append(t)
print(cold_days)
print(hot_days)  


#tuple record
student_record=("si05","khushboo",20,"AI/ML")
id,name,age,course =student_record
print(id)
print(name)
print(age)
print(course)

#book inventory
inventory={"pythonguide":12,"maths for ml":5,"ai basics":8}
print(inventory)
if "datascience handbook" not in inventory:
  inventory["datascience handbook"]=10
inventory["maths for ml"]-=3
print(inventory) 

#duplicate values

python_workshop=["cake","berry","apple","cherry"]
AI_workshop=["potato","onion","apple","cherry"]
list1=set(python_workshop)
list2=set(AI_workshop)
print(list1.intersection (list2))
print(list1.union(list2))
print(list1-list2)

#shoppping card
while True:

 print("1.add item")
 print("2.show total")
 print("3.checkout")
 print("4.exit") 
 choice=input("enter choice ")

if choice =="1":
  item_name=input("enter name:")
  item_price=float("enter price:")
  item_quantity=int("enter quantity:")
  total+=item_price*item_quqntity 

  item_count+=1
elif choice=="2":
   if item_count==0:
      print("cartis empty!")
   else:
      print(f"items in cart:{item_count}")
      print(f"total amount:rs.{total}")
   elif choice=="3":
   if item_count==0:
      print("cart is empty!add items first.")
   else:
      print(f"\n total bill : rs.{total:.2f}")
      print("1.pay")
      print("2.cancel")
      pay_choice=input("enter choice:")
      if pay_choice=="1":
         print(f"payment of rs.{total:.2f}sucessfull!")
         print(f"thanku for shopping!")
         total-0
         item_count=0
      elif pay_choice=="2":
         print("payment cancelled")
      else:
         print("invalied choice":)
      elif choice=="4":
      print("exit":)
      break;



      #shopping cart
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

    elif choice == "3":
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
       # print("Invalid choice")
 







