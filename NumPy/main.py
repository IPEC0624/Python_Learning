import numpy as np 

# video1
# print(np.__version__)

# normal python list
my_list = [1, 2, 3, 4]

my_list = my_list*2

print(my_list)

# numpy list
array = np.array([1, 2, 3, 4, 5], )

array = array * 2

print(array)

print(type(array))

# video2
array = np.array([1.1, 2.2, 3.3, 4.4, 5.5], )

array = array.astype(np.float16)

print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")

# video3
array = np.array([[['A', 'B', 'C'],['D', 'B', 'C'],['A', 'B', 'C']],
                    [['A', 'B', 'C'],['A', 'B', 'C'],['A', 'B', 'C']],
                    [['S', 'B', 'C'],['A', 'B', 'C'],['A', 'B', 'C']]
                    ])

print(array.ndim)

print(array.shape)

# Chain indexing (slower)
print(array[0][0][0])

# multidimentional indexing (faster)
print(array[0, 1, 0])

word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]

print(word)

# video4
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

array = array.reshape(1, -1)

print(array)

# video5
array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# slicing
print(array[2:, 2:])

#video6

array = np.array([1.01, 2.5, 3.99])

# Scalar arithmetic
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 4)

# Vectorized math functions
print(np.sqrt(array))
# round the num
print(np.round(array))
# convert it into the small int 
print(np.floor(array))
# convert it into the big int
print(np.ceil(array))
# PI
print(np.pi)

radius = np.array([1, 2, 3])

# area
print(np.pi * radius ** 2)

# Element-wise arithmetic
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# Comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores >= 60)

scores[scores < 60] = 0

print(scores)

# video7
array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)

# matrix broadcasting
print(array1 * array2)

array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array1 * array2)

# video8 functions
array = np.zeros((2, 3, 10))
print(array)

array = np.ones((2, 3, 10))
print(array)

array = np.full((2, 3, 10), 9)
print(array)

array = np.eye(4)
print(array)

array = np.empty((2, 3))
print(array)

array = np.arange(0, 100, 0.1)
print(array)

array = np.linspace(0, 1000, 1001)
print(array)

# video9 Aggregate functions
array = np.array([[1, 2, 3, 4, 5] , [6, 7, 8, 9, 10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array))
print(np.argmax(array))
print(np.sum(array, axis=1))

# video10 filtering
ages = np.array([[21, 17, 19, 20 ,16, 30, 18, 65], 
                 [39, 22, 15, 99, 18, 19, 20, 21]])

# filtering
teenagers = ages[ages < 18]
adults = ages[(ages >= 18) | (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0] 
odds = ages[ages % 2 != 0] 
print(teenagers)
print(adults)
print(seniors)
print(evens)
print(odds)

# where
adults = np.where(ages >= 18, ages, -1)

print(adults)

# video11 generate random numbers
rng = np.random.default_rng()

# integers
print(rng.integers(low=1, high=101, size=(3, 2)))

np.random.seed(seed=1)

# float
print(np.random.uniform(low=-1, high=1, size=(3, 2)))


# shuffle
rng = np.random.default_rng()

array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

# choice
fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
fruits = rng.choice(fruits, size=(3, 2))
print(fruits)

# video12 Save a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6]])

# save(single array)
np.save("C:\\Users\\", array)

print("NumPy array was saved!")

# load(single array)
array = np.load("C:\\Users\\data.npy")

print(array)

# save(multiple arrays)
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([1.1, 2.2, 3.3, 4.4])

# np.savez("C:\\Users\\dataz", array1, array2)
# np.savez_compressed("C:\\Users\\dataz", array1, array2)

# print("NumPy arrays were saved!")

# load(multiple arrays)
arrays = np.load("C:\\Users\\dataz.npz")

array1 = arrays["arr_0"]
array2 = arrays["arr_1"]

print(array2)






