print("hello")

apple_price = 100
print(apple_price)

apple_price = 200
print(apple_price)

x = 10
y = 100
x = y
print(x)

x = 100
x_type = type(x)
print(x_type)

x = "10"
print(type(x))
y = int(x)
print(type(y))

print(2 ** 10)
print(10 % 6)

x = 10
y = 30
z = x + y
print(z)

math = 82
japanese = 74
english = 60
avg_score = (math + japanese + english) / 3
print(avg_score)

# print(100/0)

price = 100
text = f"この商品は{price}円です"
print(text)

x = [20, 12, 40]
x.append(5)
print(x)
x.remove(5)
print(x)

print(max(x))
print(min(x))
print(sum(x))
print(sorted(x))
print(sorted(x, reverse=True))

x_avg = sum(x) / len(x)
print(x_avg)

prices = {"バナナ": 250, "みかん": 300, "イチゴ": 500}

prices["ぶどう"] = 400
print(prices)

fruits = list(prices.values())
print(fruits)

# quiz1
scores = {"math": 82, "japanese": 74, "english": 60, "science": 92, "society": 70}

difference = scores["science"] - scores["society"]
print(difference)
print(f"理科は社会より{difference}点高い")

avg_score = sum(list(scores.values())) / len(scores)
print(f"{avg_score}点")

x = {1, 2, 4}
x.add(7)
print(x)
x.remove(7)
print(x)
x.discard(4)
print(x)
x.discard(4)
# x.remove(7)

x = {0, 1, 3, 6}
y = {0, 2, 5, 6}

z = x | y
print(z)
z = x - y
print(z)
z = x & y
print(z)

fruits = ["banana", "apple", "peach"]
x = "apple"
if (x in fruits):
    print("good")

# list, set, tuple
scores = [90, 30, 49] 

for x in scores:
    print(x)
    print(x + 1)

fruits = {"apple": 130, "banana": 350, "lemon": 100}

for name, price in fruits.items():
    print(f"{name}は{price}円です")

numbers = [10, 21, 32, 65]

for n in numbers:
    print(f"{n}: 前処理")
    if n % 2 == 0:
        continue
    print(f"{n}: 後処理")
    
year = 2026

if year % 400 == 0:
    print("閏年です")
elif year % 100 == 0:
    print("平年です")
elif year % 4 == 0:
    print("閏年です")
else:
    print("平年です")
# if year % 4 == 0:
#     print("閏年です")
#     if year % 100 == 0 and not(year % 400 == 0) :
#         print("平年です")
#     else:
#         print("閏年です")
# else:
#     print("平年です")

for num in range(1, 101):
    print(num)
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")

def add_numbers(a, b):
    c = a + b
    return c

print(add_numbers(100, 100))

def add_sub_numbers(a, b):
    c = a + b
    d = a - b
    return c, d

added, subed = add_sub_numbers(100, 10)
x = add_sub_numbers(100, 10)
print(added)
print(subed)
print(x)