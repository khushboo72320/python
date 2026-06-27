fruits=("apple","banana","orange","cherry")
target ="orange" 
for fruit in fruits: 
  if fruit == target: 
   print(f"found {target}|")
   break
else:
 print(f"{target} not found in the list")