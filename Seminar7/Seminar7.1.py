my_objects = ['dfg', 'efv', 'gjk', 'd45']

#objects = [2, 4, 8, 0, 10]


# def characteristic(num: int) -> bool:
#     return num % 2 == 0

def characteristic_2(string: str) -> int:
    return len(string)


# def same_by(characteristic, objects) -> bool:
#     res = characteristic(objects[0])
#     for i in range(1, len(objects)):
#         if res != characteristic(objects[i]): return False
#     return True

def same_by(characteristic, objects) -> bool:
    if len(set(map(characteristic, objects))) <= 1: return True
    else: return False

print(same_by(characteristic_2, my_objects))
