
from typing import List

def is_polindrome(s):
    s = str(s)
    return s == s[::-1]

print(is_polindrome(333))

def slice(s):
    print(s[::-1])
    print(567 % 100)
    print(5 // 2)
    print(5 / 2)
    print(6 // 2)

slice('fggshsggjjhh')

def has_duplicates(nums):
    print(nums)
    print(set(nums))
    try:
        return len(nums) != len(set(nums))
    except TypeError:
        return False
    
print(has_duplicates([1, 3, 4, 77, 3]))


#Boyer–Moore Majority Vote Algorithm: Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may ass
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        major_el = 0

        for num in nums:
            if count == 0:
                major_el = num
            count += 1 if num == major_el else -1

        return major_el

x = 5
print(type(x))
x = "srings"
print(type(x))   


def all_unique(nums: list[int]) -> bool:
    return len(nums) == len(set(nums))


print(all_unique([1, 2, 5, 6]))


def reverse_integer(n: int) -> int:
    reverse = 0

    while n > 0:
        dig = n % 10
        reverse = reverse * 10 + dig
        n = n // 10
    return reverse

print(reverse_integer(234567))


def count_frequencies(lst: list[int]) -> dict[int, int]:
    freq_dict = {}
    for x in lst:
        if x in freq_dict:
            freq_dict[x] += 1
        else:  
            freq_dict[x] = 1  
    
    return freq_dict


print(count_frequencies([3, 55, 7, 8, 99, 99]))


def is_list_palindrome(lst: list[int]) -> bool:
    return lst == lst[::-1]



def find_min_max(lst: list[int]) -> tuple[int, int]:
    min_val = max_val = lst[0]
    for x in lst:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x

    return (min_val, max_val)


def all_even(nums: list[int]) -> bool:
    for x in nums:
        if x % 2 != 0:
            return False
        
    return True

print(all_even([2, 4, 6]))


def count_unique(nums: list[int]) -> int:

    return len(set(nums))


print(count_unique([1, 1, 3, 5]))


def last_n_elements(lst: list[int], n: int) -> list[int]:
    return lst[-n:]


def is_strictly_increasing(lst: list[int]) -> bool:
    for n in lst:
        return n[i-1] < n[i]



def replace_negatives(lst: list[int]) -> list[int]:
    
    return (0 if n < 0 else n for n in lst)


#Переверни рядок
#	•	Вхід: "Hello"
#	•	Вихід: "olleH"
#	•	Що перевіряють: робота з рядками, зрізи (s[::-1]), цикли
def reverse_order(s: str) -> str:
    return s[::-1]


def reverse_order2(s: str) -> str:
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_order("Hello"))
print(reverse_order2("Hello"))
print(type([]))


#2. Паліндром
	# •	Вхід: "level"
	# •	Вихід: True
	# •	Що перевіряють: уміння працювати з рядками та перевіряти умови.





# 3. Підрахунок символів
# 	•	Вхід: "banana"
# 	•	Вихід: {'b': 1, 'a': 3, 'n': 2}
# 	•	Що перевіряють: словники, ітерація.

# ⸻

# 4. Видалення дублікатів зі списку
# 	•	Вхід: [1, 2, 2, 3, 4, 4]
# 	•	Вихід: [1, 2, 3, 4]
# 	•	Що перевіряють: множини (set), списки.

# ⸻

# 5. Перевірка анаграм
# 	•	"listen", "silent" → True
# 	•	Що перевіряють: сортування, колекції.

# ⸻

# 6. Максимальне число у списку
# 	•	[1, 5, 2, 9, 3] → 9
# 	•	Що перевіряють: цикли, вбудовані функції (max).

# ⸻

# 7. FizzBuzz (класика)
# 	•	Вивести числа від 1 до 20, замінюючи:
# 	•	кратні 3 на "Fizz",
# 	•	кратні 5 на "Buzz",
# 	•	кратні 15 на "FizzBuzz".
# 	•	Що перевіряють: умови, модуль %.

# ⸻

# 8. Пошук другого найбільшого числа
# 	•	[10, 20, 4, 45, 99] → 45
# 	•	Що перевіряють: сортування, множини.

# ⸻

# 9. Розворот списку без reverse()
# 	•	[1, 2, 3, 4] → [4, 3, 2, 1]
# 	•	Що перевіряють: зрізи, цикли.

# ⸻

# 10. Підрахунок голосних у рядку
# 	•	"Hello World" → 3
# 	•	Що перевіряють: робота з умовами, перебір символів.