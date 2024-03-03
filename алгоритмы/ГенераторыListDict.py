items = ["10", "20", "30", "1", "11", "100"]

vlans = [int(vl) for vl in items]
#идентично
vlans = []
for vl in items:
    vlans.append(int(vl))

print(vlans)



d = {}

for num in range(1, 11):
    d[num] = num**2
#идентично
d = {num: num**2 for num in range(1, 11)}