corridor = ["Closed"]
for i in range(99):
    corridor += ["Closed"]

step = 1
while step <= len(corridor):
    door = step - 1
    while door < len(corridor):
        if corridor[door] == "Closed":
            corridor[door] = "Open"
        else:
            corridor[door] = "Closed"
        door += step
    step += 1

for i in range(len(corridor)):
    if corridor[i] == "Open":
        print (i+1, "  is open")
