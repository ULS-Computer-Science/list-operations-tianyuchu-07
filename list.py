Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
#task 1
terry_1 = ['tyy' , 'chu' , 'yrret']
print(len(terry_1))
terry_2 = input('Enter a new stuff: ')
terry_1.append(terry_2)
print((len(terry_1))

#task 2
list_1=['apple','orange','banana','cherry','watermelon']
list_1.insert(1,'grape')
print(list_1)

#task 3
row = ['_'] * 3
add_on = ['X', 'O']
final_row = row + add_on
print(final_row)

#task 4
backpack = ['book', 'pen']
found_items = ['apple', 'map']
print("Before:", backpack, found_items)
backpack.extend(found_items)
print("After:", backpack)

#task 5
number = [1, 2, 2, 2, 0]
print("Count 2:", number.count(2))
number.remove(2)
print("Count 2 after remove:", number.count(2))
      
#task 6
VIP_guests = ["terry", "chu", "tyy","yyt","yrret"]
kicked_out = VIP_guests.pop(0)
print(f"We removed[kicked_out] from the party.")
print("VIP Guest:", vip_guests)

#task 7
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del numbers[3:6]
print(numbers)

#task 8
items = ["terry", "tyy", "yrret"]
find = input("Type an item to find: ")
if find in items:
    print("Index: {items.index(find)}")
else:
    print("Safe!That item is not in the list.")

#task 9
import random
random_nums = [random.randint(1, 1000) for _ in range(5)]
random_nums.sort()
print("Sort:", random_nums)
random_nums.reverse()
print("Revers(High to Low):", random_nums)

#task 10
original = [1, 2, 3]
backup = original.copy()
original.clear()
print("Original:", original)
print("Backup:", backup)

#task 11
import random
m8b_answers = ["Yes", "No", "Maybe","neither"]
for _ in range(3):
    print(random.choice(m8b_answers))

#task 12
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])
