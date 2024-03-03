def revenue(click, price):
    revenue = 0
    while click:
        p = click.index(max(click))
        q = price.index(max(price))
        revenue += click[p] * price[q]
        click.pop(p)
        price.pop(q)
    return revenue

a = int(input())
click = list(map(int, input().split()))
price = list(map(int, input().split()))
print (revenue(click, price))