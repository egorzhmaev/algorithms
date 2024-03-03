def IsBetter(number, max_number):
    first = int(str(number)+str(max_number))
    second = int(str(max_number)+str(number))
    if first > second:
        return True
    else:
        return False
def largest_concatenate(numbers):
    your_salary = ""
    while numbers:
        max_number = numbers[0]
        for number in numbers:
            if IsBetter(number, max_number):
                max_number = number
        your_salary += str(max_number)
        numbers.remove(max_number)
    return your_salary

n = int(input())
a = list(map(int, input().split()))
print(largest_concatenate(a))