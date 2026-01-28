import copy

def translate_roman_to_integer(roman_numeral):
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    length = len(roman_numeral)

    for i in reversed(range(length)):
        if roman_numeral[i] not in roman_to_int_map:
            raise TypeError
        numeral = roman_numeral[i]
        value = roman_to_int_map[roman_numeral[i]]

        if i + 1 < length and numeral in {"V", "L", "D"}:
            if numeral == roman_numeral[i+1]:
                raise ValueError("Not allowed to repeat V L D. Got: " + numeral + " and " + roman_numeral[i-1])
        elif i + 3 <= length:

            y = i
            repeat_count = 0
            while y < length:
                if roman_numeral[y] != numeral:
                    break
                else:
                    y += 1
                    repeat_count += 1
                    if repeat_count > 3:
                        raise ValueError("Not allowed to repeat " + numeral + " more than 3 times.")

        if i < length -1:
            if value < roman_to_int_map[roman_numeral[i+1]]:
                if numeral in {"I", "X", "C"}:
                    total -= value
                else:
                    raise ValueError("Not allowed to subtract with " + numeral)
                continue

        total += value

    if total >= 4000:
        raise ValueError("Value can't be greater than 4000")

    return total