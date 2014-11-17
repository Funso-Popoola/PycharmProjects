__author__ = 'funso'


dico = {"Anchovies":50, "Artichoke":60, "Bacon":92, "Broccoli":24, "Cheese":80, "Chicken":30, "Feta":99, "Garlic":8, "Ham":46, "Jalapeno": 5, "Meatballs":120, "Mushrooms":11, "Olives":25, "Onions":11, "Pepperoni":80, "Peppers":6, "Pineapple":21, "Ricotta":108, "Sausage":115, "Spinach": 18, "Tomatoes":14}

#read
raw = raw_input().strip("\n")
raw = raw.strip("\r")
raw = raw.split(" ")

n = int(raw[0])
i = 1
k = 1
top = []
while ( i <= n):
    num = int(raw[k])
    k += 1
    item = []
    item.append(num)
    item.append(raw[k].split(","))
    top.append(item)
    k += 1
    i += 1

total = 0
for each in top:
    kt = each[0]
    sub_total = 0
    for ind in each[1]:
        sub_total += (dico.get(ind))
    total += kt * (sub_total + 270)

print total