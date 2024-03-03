def get_card_count(n, k, cards) -> int:
    result = 0
    i = j = 0
    summ1 = sum(cards[i:k])
    summ2 = sum(card[j:k])
    n = m = k
    while k > 0:
        if summ1 >= summ2:
            result += cards[i]
            summ1 -= cards[i]
            n -= 1
            summ2 -= card[n]
            i += 1
            k -= 1
        else:
            result += card[j]
            m -= 1
            summ1 -= cards[m]
            summ2 -= card[j]
            j += 1
            k -= 1
    return result

n = int(input())
k = int(input())
cards = list(map(int, input().split()))
card = list(reversed(cards))
print (get_card_count(n, k, cards))
