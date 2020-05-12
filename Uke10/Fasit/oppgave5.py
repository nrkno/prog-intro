def min_sum(*tall):
    sum = 0
    for t in tall: 
        sum = sum + t
    return sum

print(min_sum(1, 5, 10, 0, 15, 4.4))