def convert_to_arabic(number: str) -> int:
    if not number:
        return -1
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    min = 0
    arr = list()
    while i < len(number):
        if i+1 < len(number):
            if roman_numerals[number[i]] < roman_numerals[number[i+1]]:
                if roman_numerals[number[i]] == 100 and roman_numerals[number[i+1]] == 1000 or roman_numerals[number[i+1]] == 500:
                    result += roman_numerals[number[i+1]] - roman_numerals[number[i]]
                    arr.append(roman_numerals[number[i+1]] - roman_numerals[number[i]])
                    i += 2
                elif roman_numerals[number[i]] == 10 and roman_numerals[number[i+1]] == 100 or roman_numerals[number[i+1]] == 50:
                    result += roman_numerals[number[i+1]] - roman_numerals[number[i]]
                    arr.append(roman_numerals[number[i + 1]] - roman_numerals[number[i]])
                    i += 2
                elif roman_numerals[number[i]] == 1 and roman_numerals[number[i+1]] == 5 or roman_numerals[number[i+1]] == 10:
                    result += roman_numerals[number[i+1]] - roman_numerals[number[i]]
                    arr.append(roman_numerals[number[i + 1]] - roman_numerals[number[i]])
                    i += 2
                else:
                    i += len(number)
                    min += 1
            else:
                result += roman_numerals[number[i]]
                arr.append(roman_numerals[number[i]])
                i += 1
        else:
            result += roman_numerals[number[i]]
            arr.append(roman_numerals[number[i]])
            i += 1
    j = 1
    while j < len(arr):
        if arr[j-1] < arr[j]:
            min += 1
        if arr[j-1] == 9 and arr[j] == 9:
            min += 1
        if arr[j-1] == 90 and arr[j] == 90:
            min += 1
        if arr[j-1] == 900 and arr[j] == 900:
            min += 1
        if arr[j-1] == 4 and arr[j] == 4:
            min += 1
        if arr[j-1] == 40 and arr[j] == 40:
            min += 1
        if arr[j-1] == 400 and arr[j] == 400:
            min += 1
        j += 1

    if min > 0:
        return -1

    if number.count('V') > 1:
        return -1
    if number.count('L') > 1:
        return -1
    if number.count('D') > 1:
        return -1

    if "IIII" in number:
        return -1
    if "XXXX" in number:
        return -1
    if "CCCC" in number:
        return -1
    if "MMMM" in number:
        return -1

    return result

roman_number = input()
print(convert_to_arabic(roman_number))