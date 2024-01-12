import numpy as np

def rule_value(rule):
    rule_value = np.array([], dtype=np.int16)
    while rule > 0:
        rule_value = np.append(rule_value, rule % 2)
        rule = rule // 2

    while len(rule_value) < 8:
        rule_value = np.append(rule_value, 0)

    rule_value = rule_value[::-1]
    return rule_value

def calc_state(array, rule):
    new_array = np.array([], dtype=np.int16)
    for i in range(len(array)):
        if i == 0 or i == len(array) - 1:
            new_array = np.append(new_array, array[i])
        else:
            a, b, c = array[i-1], array[i], array[i+1]
            new_value = a*2**2+b*2**1+c
            new_array = np.append(new_array, rule[7-new_value])
    return new_array