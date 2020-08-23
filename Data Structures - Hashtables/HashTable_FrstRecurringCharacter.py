def firstRecurringChar(array):
    collector = set()
    for item in array:
        if item not in collector:
            collector.add(item)
        else:
            return item
    return "Undefined"

array = [2,3,4,5]
print(firstRecurringChar(array))